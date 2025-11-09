"""
Improved reward function for Pwnagotchi AI
Balances handshake capture with system stability
"""
import pwnagotchi.mesh.wifi as wifi

# Reward range for RL algorithm
range = (-1.0, 1.2)

# Avoid division by zero
EPSILON = 1e-20


class RewardFunction:
    """
    Calculates reward based on WiFi capture performance and stability

    Improvements over original:
    - More balanced weights to prevent aggressive behavior
    - Stability bonus for consistent operation
    - Lower penalty for conservative strategies
    """

    def __call__(self, epoch_n, state):
        """
        Calculate reward for current epoch

        Args:
            epoch_n: Current epoch number
            state: Dictionary with epoch statistics

        Returns:
            Float reward value in range
        """
        tot_epochs = epoch_n + EPSILON
        tot_interactions = max(
            state['num_deauths'] + state['num_associations'],
            state['num_handshakes']
        ) + EPSILON
        tot_channels = wifi.NumChannels

        # Positive rewards (what we want)
        # Handshakes are the primary goal, but weighted more conservatively
        handshakes = 0.7 * (state['num_handshakes'] / tot_interactions)

        # Active time is good (but don't over-reward constant activity)
        active = 0.15 * (state['active_for_epochs'] / tot_epochs)

        # Channel coverage is beneficial
        coverage = 0.08 * (state['num_hops'] / tot_channels)

        # Stability bonus: reward consistent operation
        # If we've been running for a while without issues, that's good
        if epoch_n > 10:
            stability_bonus = 0.05
        else:
            stability_bonus = 0.0

        # Negative rewards (what we want to avoid)
        # Blind time (not seeing network) is bad
        blind = -0.2 * (state.get('blind_for_epochs', 0) / tot_epochs)

        # Missed interactions are bad (but less severe than original)
        missed = -0.2 * (state['missed_interactions'] / tot_interactions)

        # Inactive time is bad (but less severe to allow conservative behavior)
        inactive = -0.15 * (state['inactive_for_epochs'] / tot_epochs)

        # Emotional state penalties (if epochs >= 5)
        sad_epochs = state.get('sad_for_epochs', 0) if state.get('sad_for_epochs', 0) >= 5 else 0
        bored_epochs = state.get('bored_for_epochs', 0) if state.get('bored_for_epochs', 0) >= 5 else 0

        sad_penalty = -0.15 * (sad_epochs / tot_epochs)
        bored_penalty = -0.08 * (bored_epochs / tot_epochs)

        # WiFi crash penalty (NEW - discourage policies that crash WiFi)
        # This would need to be detected and added to state by stability monitor
        crash_penalty = -0.5 * state.get('wifi_crashes', 0)

        # Total reward
        reward = (
            handshakes + active + coverage + stability_bonus +
            blind + missed + inactive +
            sad_penalty + bored_penalty + crash_penalty
        )

        # Clamp to expected range
        return max(min(reward, range[1]), range[0])


# Default reward function instance
default_reward = RewardFunction()
