"""
WiFi stability monitoring for Pwnagotchi AI
Detects instability and triggers rollback to safe parameters
"""
import logging
import time
from collections import deque


class StabilityMonitor:
    """
    Monitors WiFi stability and detects when AI parameters cause problems

    Features:
    - Track WiFi connection health
    - Detect rapid parameter changes
    - Automatic rollback on instability
    - Rate limiting for parameter updates
    """

    def __init__(self, config):
        """
        Initialize stability monitor

        Args:
            config: AI configuration dictionary
        """
        self.config = config
        self.enabled = config.get('stability_monitoring', True)

        # Tracking
        self.wifi_errors = deque(maxlen=10)  # Last 10 error events
        self.param_changes = deque(maxlen=20)  # Last 20 parameter changes
        self.last_stable_params = None
        self.last_update_time = 0
        self.rollback_count = 0

        # Thresholds
        self.max_errors_per_minute = config.get('max_errors_per_minute', 5)
        self.min_update_interval = config.get('min_update_interval', 30)  # seconds
        self.max_param_change_rate = config.get('max_param_change_rate', 0.3)  # 30% change

        logging.info("[ai-stability] Stability monitoring enabled")

    def record_wifi_error(self):
        """Record a WiFi error event"""
        if not self.enabled:
            return

        self.wifi_errors.append(time.time())
        logging.warning("[ai-stability] WiFi error recorded")

        # Check if error rate is too high
        if self.is_unstable():
            logging.error("[ai-stability] WiFi instability detected!")
            return True

        return False

    def is_unstable(self):
        """
        Check if WiFi is currently unstable

        Returns:
            bool: True if unstable, False otherwise
        """
        if not self.enabled or len(self.wifi_errors) < 3:
            return False

        # Check error rate in last minute
        now = time.time()
        recent_errors = sum(1 for t in self.wifi_errors if now - t < 60)

        if recent_errors >= self.max_errors_per_minute:
            return True

        return False

    def should_update_params(self):
        """
        Check if enough time has passed for parameter update (rate limiting)

        Returns:
            bool: True if update is allowed, False otherwise
        """
        if not self.enabled:
            return True

        now = time.time()
        time_since_last = now - self.last_update_time

        if time_since_last < self.min_update_interval:
            logging.debug(
                f"[ai-stability] Rate limiting: {time_since_last:.1f}s < {self.min_update_interval}s"
            )
            return False

        return True

    def validate_param_change(self, old_params, new_params):
        """
        Validate that parameter changes aren't too extreme

        Args:
            old_params: Previous parameter dict
            new_params: Proposed new parameter dict

        Returns:
            bool: True if change is safe, False if too extreme
        """
        if not self.enabled or old_params is None:
            return True

        # Check numeric parameters for large changes
        for key in new_params:
            if key == 'channels':
                continue  # Skip channel list

            if key in old_params:
                old_val = old_params[key]
                new_val = new_params[key]

                # For numeric values, check relative change
                if isinstance(old_val, (int, float)) and isinstance(new_val, (int, float)):
                    if old_val != 0:
                        relative_change = abs(new_val - old_val) / abs(old_val)
                        if relative_change > self.max_param_change_rate:
                            logging.warning(
                                f"[ai-stability] Large change in {key}: "
                                f"{old_val} -> {new_val} ({relative_change:.1%})"
                            )
                            return False

        return True

    def apply_smoothing(self, old_params, new_params, alpha=0.5):
        """
        Apply exponential smoothing to parameter changes

        Args:
            old_params: Previous parameter dict
            new_params: Proposed new parameter dict
            alpha: Smoothing factor (0 = keep old, 1 = use new)

        Returns:
            dict: Smoothed parameters
        """
        if not self.enabled or old_params is None:
            return new_params

        smoothed = {}

        for key, new_val in new_params.items():
            if key == 'channels':
                # Don't smooth channel lists, use new value
                smoothed[key] = new_val
            elif key in old_params:
                old_val = old_params[key]
                # Apply exponential smoothing for numeric values
                if isinstance(old_val, (int, float)) and isinstance(new_val, (int, float)):
                    smoothed_val = alpha * new_val + (1 - alpha) * old_val
                    # Preserve type (int vs float)
                    if isinstance(new_val, int):
                        smoothed[key] = int(round(smoothed_val))
                    else:
                        smoothed[key] = smoothed_val
                else:
                    smoothed[key] = new_val
            else:
                smoothed[key] = new_val

        return smoothed

    def update_params(self, params):
        """
        Record parameter update

        Args:
            params: New parameters being applied
        """
        if not self.enabled:
            return

        self.last_update_time = time.time()
        self.param_changes.append((time.time(), params.copy()))

        # Store as stable params if no recent errors
        if not self.is_unstable():
            self.last_stable_params = params.copy()
            logging.debug("[ai-stability] Stored stable parameters")

    def get_safe_params(self):
        """
        Get last known safe parameters for rollback

        Returns:
            dict or None: Last stable parameters
        """
        if self.last_stable_params:
            logging.info("[ai-stability] Rolling back to stable parameters")
            self.rollback_count += 1
        return self.last_stable_params

    def get_stats(self):
        """
        Get stability statistics

        Returns:
            dict: Statistics about stability
        """
        now = time.time()
        recent_errors = sum(1 for t in self.wifi_errors if now - t < 60)

        return {
            'enabled': self.enabled,
            'is_unstable': self.is_unstable(),
            'recent_errors': recent_errors,
            'rollback_count': self.rollback_count,
            'has_stable_params': self.last_stable_params is not None,
        }
