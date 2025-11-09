"""
Gymnasium-compatible environment for Pwnagotchi AI
Implements the WiFi pwning environment for reinforcement learning
"""
import logging
import numpy as np
import gymnasium as gym
from gymnasium import spaces

import pwnagotchi.ai.featurizer as featurizer
import pwnagotchi.ai.reward as reward
from pwnagotchi.ai.parameter import Parameter


class Environment(gym.Env):
    """
    Pwnagotchi WiFi environment for reinforcement learning

    Compatible with Gymnasium and stable-baselines3
    """

    metadata = {'render_modes': ['human']}

    # Parameters that the AI can tune
    params = [
        Parameter('min_rssi', min_value=-200, max_value=-50),
        Parameter('ap_ttl', min_value=30, max_value=600),
        Parameter('sta_ttl', min_value=60, max_value=300),
        Parameter('recon_time', min_value=5, max_value=60),
        Parameter('max_inactive_scale', min_value=3, max_value=10),
        Parameter('recon_inactive_multiplier', min_value=1, max_value=3),
        Parameter('hop_recon_time', min_value=5, max_value=60),
        Parameter('min_recon_time', min_value=1, max_value=30),
        Parameter('max_interactions', min_value=1, max_value=25),
        Parameter('max_misses_for_recon', min_value=3, max_value=10),
        Parameter('excited_num_epochs', min_value=5, max_value=30),
        Parameter('bored_num_epochs', min_value=5, max_value=30),
        Parameter('sad_num_epochs', min_value=5, max_value=30),
    ]

    def __init__(self, agent, epoch):
        """
        Initialize environment

        Args:
            agent: Pwnagotchi agent instance
            epoch: Epoch manager for training synchronization
        """
        super(Environment, self).__init__()

        self._agent = agent
        self._epoch = epoch
        self._epoch_num = 0
        self._last_render = None
        self._reward_fn = reward.RewardFunction()

        # Channel configuration
        self._supported_channels = agent.supported_channels()
        self._extended_spectrum = any(ch > 140 for ch in self._supported_channels)
        self._histogram_size, self._observation_shape = featurizer.describe(self._extended_spectrum)

        # Add channel parameters dynamically
        Environment.params += [
            Parameter(f'_channel_{ch}', min_value=0, max_value=1, meta=ch + 1)
            for ch in range(self._histogram_size)
            if ch + 1 in self._supported_channels
        ]

        # State tracking
        self.last = {
            'reward': 0.0,
            'observation': None,
            'policy': None,
            'params': {},
            'state': None,
            'state_v': None
        }

        # Define action and observation spaces (compatible with SB3/Gymnasium)
        trainable_params = [p for p in Environment.params if p.trainable]

        self.action_space = spaces.MultiDiscrete([p.space_size() for p in trainable_params])
        self.observation_space = spaces.Box(
            low=0.0,
            high=1.0,
            shape=self._observation_shape,
            dtype=np.float32
        )

        self.reward_range = reward.range

        logging.debug(
            f"[ai-env] Created environment: "
            f"obs_shape={self._observation_shape}, "
            f"action_space={len(trainable_params)} params"
        )

    @staticmethod
    def policy_size():
        """Get number of trainable parameters"""
        return len([p for p in Environment.params if p.trainable])

    @staticmethod
    def policy_to_params(policy):
        """
        Convert policy vector to parameter dictionary

        Args:
            policy: Array of discrete actions

        Returns:
            dict: Parameter names and values
        """
        num = len(policy)
        params = {}
        channels = []

        assert len(Environment.params) == num, \
            f"Policy size mismatch: {num} != {len(Environment.params)}"

        for i in range(num):
            param = Environment.params[i]

            if '_channel' not in param.name:
                # Regular parameter
                params[param.name] = param.to_param_value(policy[i])
            else:
                # Channel parameter (binary: include or not)
                has_chan = param.to_param_value(policy[i])
                chan = param.meta
                if has_chan:
                    channels.append(chan)

        params['channels'] = channels
        return params

    def _next_epoch(self):
        """Wait for next epoch data"""
        logging.debug("[ai-env] Waiting for epoch to finish...")
        return self._epoch.wait_for_epoch_data()

    def _apply_policy(self, policy):
        """
        Apply policy (parameter configuration) to agent

        Args:
            policy: Array of discrete actions
        """
        new_params = Environment.policy_to_params(policy)
        self.last['policy'] = policy
        self.last['params'] = new_params

        logging.debug(
            f"[ai-env] Applying policy: {len(new_params)} params, "
            f"{len(new_params.get('channels', []))} channels"
        )

        self._agent.on_ai_policy(new_params)

    def step(self, action):
        """
        Execute one timestep within the environment

        Args:
            action: Policy vector (parameter configuration)

        Returns:
            observation, reward, terminated, truncated, info
            (Gymnasium API format)
        """
        # Apply the new policy/parameters
        self._apply_policy(action)
        self._epoch_num += 1

        # Wait for the algorithm to run with new parameters
        state = self._next_epoch()

        # Calculate reward
        self.last['reward'] = self._reward_fn(self._epoch_num, state)
        self.last['state'] = state
        self.last['state_v'] = featurizer.featurize(state, self._epoch_num)

        # Notify agent of step completion
        self._agent.on_ai_step()

        # Determine if episode is done
        terminated = not self._agent.is_training()
        truncated = False  # We don't truncate episodes

        # Additional info
        info = {
            'epoch': self._epoch_num,
            'handshakes': state.get('num_handshakes', 0),
        }

        return self.last['state_v'], self.last['reward'], terminated, truncated, info

    def reset(self, seed=None, options=None):
        """
        Reset environment to initial state

        Args:
            seed: Random seed (for reproducibility)
            options: Additional options

        Returns:
            observation, info (Gymnasium API format)
        """
        super().reset(seed=seed)

        logging.debug("[ai-env] Resetting environment...")
        self._epoch_num = 0

        # Get initial state
        state = self._next_epoch()
        self.last['state'] = state
        self.last['state_v'] = featurizer.featurize(state, 1)

        info = {'epoch': self._epoch_num}

        return self.last['state_v'], info

    def _render_histogram(self, hist):
        """Pretty-print histogram of channel activity"""
        for ch in range(self._histogram_size):
            if hist[ch]:
                logging.info(f"      CH {ch + 1}: {hist[ch]}")

    def render(self, mode='human'):
        """
        Render the environment state

        Args:
            mode: Render mode (only 'human' supported)
        """
        # Avoid rendering same data twice
        if self._last_render == self._epoch_num:
            return

        if not self._agent.is_training():
            return

        self._last_render = self._epoch_num

        logging.info(
            f"[ai-env] --- Training epoch {self._epoch_num}/"
            f"{self._agent.training_epochs()} ---"
        )
        logging.info(f"[ai-env] REWARD: {self.last['reward']:.4f}")

        logging.debug(
            f"[ai-env] Policy: " +
            ', '.join(f"{k}:{v}" for k, v in self.last['params'].items())
        )

        if logging.getLogger().isEnabledFor(logging.INFO):
            logging.info("[ai-env] Observation:")
            for name, value in self.last['state'].items():
                if 'histogram' in name:
                    logging.info(f"    {name.replace('_histogram', '')}")
                    self._render_histogram(value)
                else:
                    logging.info(f"    {name}: {value}")
