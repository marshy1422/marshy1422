# Modern AI for Pwnagotchi

This implementation restores and modernizes the AI capabilities of Pwnagotchi using state-of-the-art reinforcement learning techniques.

## Overview

The original Pwnagotchi AI was removed due to WiFi firmware stability issues. This modernized version addresses those issues while providing better performance through:

- **Modern Framework**: PyTorch instead of TensorFlow 1.x
- **Better Algorithm**: PPO (Proximal Policy Optimization) instead of A2C
- **Stability Safeguards**: Built-in monitoring and rollback mechanisms
- **Configurable**: Easy to enable/disable and tune

## What's New?

### Framework Upgrades

| Component | Original | Modern |
|-----------|----------|--------|
| Deep Learning | TensorFlow 1.13.1 | PyTorch 2.0+ |
| RL Library | stable-baselines 2.7.0 | stable-baselines3 2.2+ |
| Gym | gym 0.14.0 | gymnasium 0.29+ |
| Algorithm | A2C | PPO |

### Key Improvements

1. **Stability Monitoring** (`stability.py`)
   - Tracks WiFi health in real-time
   - Rate limits parameter updates
   - Automatic rollback on instability
   - Gradual parameter smoothing

2. **Improved Reward Function** (`reward.py`)
   - More balanced weights to avoid aggressive behavior
   - Stability bonus for consistent operation
   - WiFi crash penalty
   - Lower penalties for conservative strategies

3. **Better Algorithm** (PPO vs A2C)
   - More stable training
   - Better sample efficiency
   - Less likely to cause wild parameter swings
   - Industry-standard for robotics/real-world RL

## Installation

### 1. Install Dependencies

```bash
pip install -r requirements-ai.txt
```

For Raspberry Pi (recommended to use CPU-only PyTorch):

```bash
pip install torch --index-url https://download.pytorch.org/whl/cpu
pip install stable-baselines3 gymnasium numpy
```

### 2. Enable AI in Configuration

Edit your `/etc/pwnagotchi/config.toml`:

```toml
[ai]
enabled = true
path = "/root/.pwnagotchi-ai.pt"
```

### 3. Restart Pwnagotchi

```bash
sudo systemctl restart pwnagotchi
```

## Configuration

### Basic Configuration

```toml
[ai]
enabled = false  # Set to true to enable AI
path = "/root/.pwnagotchi-ai.pt"  # Where to save the trained model
verbose = false  # Set to true for detailed AI logging
```

### Stability Monitoring

```toml
[ai]
stability_monitoring = true  # Enable stability safeguards
max_errors_per_minute = 5  # Max WiFi errors before triggering safety
min_update_interval = 30  # Minimum seconds between updates (rate limiting)
max_param_change_rate = 0.3  # Maximum 30% parameter change per update
```

### Advanced: PPO Hyperparameters

```toml
[ai.params]
learning_rate = 0.0003  # Learning rate
n_steps = 2048  # Steps collected before update
batch_size = 64  # Minibatch size
n_epochs = 10  # Training epochs per update
gamma = 0.99  # Discount factor
gae_lambda = 0.95  # GAE lambda
clip_range = 0.2  # PPO clipping parameter
ent_coef = 0.01  # Entropy coefficient (exploration)
```

## How It Works

### Parameters Tuned by AI

The AI automatically tunes these parameters to maximize handshake capture:

- `min_rssi`: Minimum signal strength to consider
- `ap_ttl`: Access point time-to-live
- `sta_ttl`: Station (client) time-to-live
- `recon_time`: Reconnaissance time
- `hop_recon_time`: Channel hop reconnaissance time
- `min_recon_time`: Minimum reconnaissance time
- `max_interactions`: Maximum interactions per epoch
- `max_misses_for_recon`: Max misses before reconnaissance
- `excited_num_epochs`: Epochs to stay excited
- `bored_num_epochs`: Epochs before becoming bored
- `sad_num_epochs`: Epochs before becoming sad
- `channels`: Which WiFi channels to monitor

### Reward Function

The AI learns by receiving rewards for good behavior:

**Positive Rewards:**
- 🎯 Handshakes captured (primary goal)
- ⚡ Active time (being productive)
- 📡 Channel coverage (exploring spectrum)
- 🛡️ Stability bonus (running without crashes)

**Negative Penalties:**
- 👻 Blind epochs (not seeing networks)
- ❌ Missed interactions
- 😴 Inactive time
- 😢 Sad/bored emotional states
- 💥 WiFi crashes (NEW - prevents instability)

### Stability Safeguards

1. **Rate Limiting**: Won't update parameters more than once per `min_update_interval` seconds
2. **Change Validation**: Rejects extreme parameter changes (>30% by default)
3. **Parameter Smoothing**: Applies exponential smoothing to gradual changes
4. **Health Monitoring**: Tracks WiFi errors and triggers rollback if unstable
5. **Safe Mode**: Falls back to last known stable parameters

## Monitoring

### Check AI Status

```bash
# View logs
tail -f /etc/pwnagotchi/log/pwnagotchi.log | grep "\[ai"

# Look for:
# [ai] AI loaded successfully
# [ai-env] Training epoch X/Y
# [ai-env] REWARD: 0.xxxx
# [ai-stability] Stability monitoring enabled
```

### Interpreting Rewards

- **Positive rewards** (> 0): AI is learning good behavior
- **Negative rewards** (< 0): AI is being penalized
- **Increasing over time**: AI is improving
- **Stable around 0.5-0.8**: AI has found a good policy

### Troubleshooting

**AI not loading?**
- Check dependencies: `pip list | grep -E "torch|stable-baselines3|gymnasium"`
- Check logs: `grep "\[ai\]" /etc/pwnagotchi/log/pwnagotchi.log`

**WiFi becoming unstable?**
- Increase `min_update_interval` (slow down learning)
- Decrease `max_param_change_rate` (smaller changes)
- Check `[ai-stability]` logs for rollback events

**Poor performance?**
- Let it train longer (100+ epochs)
- Enable verbose logging: `verbose = true`
- Check reward trends in logs

## Technical Details

### Architecture

```
Agent (agent.py)
  └─> Epoch Tracker (epoch.py)
       └─> Environment (gym.py)
            ├─> Featurizer (featurizer.py)
            ├─> Reward Function (reward.py)
            └─> PPO Model (__init__.py)
                 └─> Stability Monitor (stability.py)
```

### Files Added/Modified

**New Files:**
- `pwnagotchi/ai/__init__.py` - PyTorch/SB3 model loader
- `pwnagotchi/ai/parameter.py` - Parameter management
- `pwnagotchi/ai/featurizer.py` - Feature extraction
- `pwnagotchi/ai/gym.py` - Gymnasium environment
- `pwnagotchi/ai/stability.py` - Stability monitoring (NEW)
- `requirements-ai.txt` - AI dependencies

**Modified Files:**
- `pwnagotchi/ai/reward.py` - Improved reward function
- `pwnagotchi/defaults.toml` - Added [ai] configuration section

**Preserved Files:**
- `pwnagotchi/ai/epoch.py` - Epoch tracking (unchanged)

## Comparison: Original vs Modern

### Original AI Issues
- ❌ WiFi firmware instability
- ❌ Aggressive parameter changes
- ❌ Outdated TensorFlow 1.x
- ❌ A2C algorithm (less stable)
- ❌ No safety mechanisms

### Modern AI Solutions
- ✅ Stability monitoring & rollback
- ✅ Gradual parameter smoothing
- ✅ Modern PyTorch 2.x
- ✅ PPO algorithm (more stable)
- ✅ Multiple safety safeguards

## Performance Tips

1. **Start Conservative**: Use default stability settings initially
2. **Monitor First 50 Epochs**: Watch for instability patterns
3. **Adjust Gradually**: If stable, can decrease `min_update_interval` for faster learning
4. **Location Matters**: AI learns location-specific patterns (home vs work)
5. **Be Patient**: Good policies take 100-200 epochs to develop

## Contributing

Found a bug or have improvements? Please submit issues or PRs!

## License

Same as Pwnagotchi - GPL-3.0

## Credits

- **Original Pwnagotchi AI**: @evilsocket
- **Modern PyTorch Implementation**: This fork
- **jayofelony/pwnagotchi**: Base fork without AI
- **stable-baselines3**: RL algorithms
- **PyTorch**: Deep learning framework

---

**Note**: This AI is experimental. Always monitor your device when first enabling it. The stability safeguards should prevent crashes, but feedback is welcome!
