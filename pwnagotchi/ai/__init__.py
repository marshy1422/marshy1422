"""
Modern PyTorch-based AI for Pwnagotchi
Uses stable-baselines3 with PPO algorithm
"""
import os
import time
import logging

# Suppress TensorFlow warnings (if any dependencies still use it)
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


def load(config, agent, epoch, from_disk=True):
    """
    Load and initialize the AI model

    Args:
        config: Full configuration dictionary
        agent: Pwnagotchi agent instance
        epoch: Epoch manager for training
        from_disk: Whether to load existing model from disk

    Returns:
        Trained model instance or False if AI is disabled/failed
    """
    ai_config = config['ai']

    if not ai_config['enabled']:
        logging.info("[ai] AI disabled in configuration")
        return False

    try:
        begin = time.time()
        logging.info("[ai] Bootstrapping modern AI (PyTorch + PPO)...")

        # Import dependencies (lazy import to speed up startup when AI is disabled)
        start = time.time()
        from stable_baselines3 import PPO
        logging.debug(f"[ai] PPO imported in {time.time() - start:.2f}s")

        start = time.time()
        from stable_baselines3.common.vec_env import DummyVecEnv
        logging.debug(f"[ai] DummyVecEnv imported in {time.time() - start:.2f}s")

        start = time.time()
        import pwnagotchi.ai.gym as wrappers
        from pwnagotchi.ai.stability import StabilityMonitor
        logging.debug(f"[ai] Gym wrapper imported in {time.time() - start:.2f}s")

        # Create environment
        logging.info("[ai] Creating environment...")
        env = wrappers.Environment(agent, epoch)
        env = DummyVecEnv([lambda: env])

        # Initialize stability monitor
        stability_monitor = StabilityMonitor(ai_config)
        agent._stability_monitor = stability_monitor

        # Configure PPO model
        logging.info("[ai] Creating PPO model...")
        start = time.time()

        # PPO hyperparameters (optimized for stability)
        ppo_params = ai_config.get('params', {})
        default_params = {
            'learning_rate': 3e-4,
            'n_steps': 2048,
            'batch_size': 64,
            'n_epochs': 10,
            'gamma': 0.99,
            'gae_lambda': 0.95,
            'clip_range': 0.2,
            'clip_range_vf': None,
            'ent_coef': 0.01,  # Encourage exploration
            'vf_coef': 0.5,
            'max_grad_norm': 0.5,
            'verbose': 1 if ai_config.get('verbose', False) else 0,
        }

        # Merge user params with defaults
        merged_params = {**default_params, **ppo_params}

        # Create PPO model
        model = PPO(
            policy="MlpPolicy",  # Simple MLP policy (no LSTM for now, for stability)
            env=env,
            **merged_params
        )

        logging.debug(f"[ai] PPO created in {time.time() - start:.2f}s")

        # Load existing model if available
        model_path = ai_config['path']
        if from_disk and os.path.exists(model_path):
            logging.info(f"[ai] Loading model from {model_path}...")
            start = time.time()
            model = PPO.load(model_path, env=env)
            logging.debug(f"[ai] Model loaded in {time.time() - start:.2f}s")
        else:
            logging.info("[ai] Model created with parameters:")
            for key, value in merged_params.items():
                logging.info(f"      {key}: {value}")

        total_time = time.time() - begin
        logging.info(f"[ai] AI loaded successfully in {total_time:.2f}s")

        return model

    except ImportError as e:
        logging.error(
            f"[ai] Failed to import required AI libraries: {e}\n"
            f"[ai] Please install: pip install torch stable-baselines3 gymnasium"
        )
        return False

    except Exception as e:
        logging.exception(f"[ai] Error while starting AI: {e}")
        return False


def save(model, path):
    """
    Save model to disk

    Args:
        model: Trained model instance
        path: Path to save model
    """
    try:
        logging.info(f"[ai] Saving model to {path}...")
        model.save(path)
        logging.info("[ai] Model saved successfully")
        return True
    except Exception as e:
        logging.error(f"[ai] Error saving model: {e}")
        return False
