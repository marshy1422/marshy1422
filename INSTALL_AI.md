# Easy Installation Guide - Pwnagotchi Modern AI

This guide will walk you through installing the modern AI on your Pwnagotchi device.

## Prerequisites

- A working Pwnagotchi device (Raspberry Pi with Pwnagotchi installed)
- SSH access to your Pwnagotchi
- Internet connection on your Pwnagotchi

## Step 1: Connect to Your Pwnagotchi

SSH into your Pwnagotchi:

```bash
ssh pi@10.0.0.2
# Default password is usually "raspberry"
```

## Step 2: Backup Your Current Setup (Optional but Recommended)

```bash
sudo cp /etc/pwnagotchi/config.toml /etc/pwnagotchi/config.toml.backup
```

## Step 3: Install AI Dependencies

Run this command to install the required Python packages:

```bash
sudo pip3 install torch --index-url https://download.pytorch.org/whl/cpu
sudo pip3 install stable-baselines3 gymnasium numpy
```

**Note:** This may take 10-20 minutes on a Raspberry Pi Zero. Be patient!

## Step 4: Update Your Pwnagotchi Code

If you're using this modified version, copy the AI files to your Pwnagotchi:

```bash
# Create AI directory if it doesn't exist
sudo mkdir -p /usr/local/lib/python3.*/dist-packages/pwnagotchi/ai/

# Copy the AI files
# (You'll need to transfer the files from this repo to your Pwnagotchi)
```

**OR** if you cloned this repo on your Pwnagotchi:

```bash
cd /path/to/this/repo
sudo cp -r pwnagotchi/ai/* /usr/local/lib/python3.*/dist-packages/pwnagotchi/ai/
```

## Step 5: Enable AI in Configuration

Edit your Pwnagotchi config file:

```bash
sudo nano /etc/pwnagotchi/config.toml
```

Add or modify the `[ai]` section:

```toml
[ai]
enabled = true  # Change this from false to true
path = "/root/.pwnagotchi-ai.pt"
verbose = false  # Set to true if you want detailed AI logs

# Stability monitoring (prevents WiFi crashes)
stability_monitoring = true
max_errors_per_minute = 5
min_update_interval = 30
max_param_change_rate = 0.3

[ai.params]
learning_rate = 0.0003
n_steps = 2048
batch_size = 64
n_epochs = 10
gamma = 0.99
gae_lambda = 0.95
clip_range = 0.2
ent_coef = 0.01
```

Press `Ctrl+X`, then `Y`, then `Enter` to save.

## Step 6: Restart Pwnagotchi

```bash
sudo systemctl restart pwnagotchi
```

## Step 7: Monitor the AI

Watch the logs to see if the AI loaded successfully:

```bash
sudo tail -f /var/log/pwnagotchi.log | grep "\[ai"
```

You should see messages like:
- `[ai] Bootstrapping modern AI (PyTorch + PPO)...`
- `[ai] AI loaded successfully`
- `[ai-env] Training epoch X/Y`
- `[ai-stability] Stability monitoring enabled`

## Troubleshooting

### AI Not Loading?

**Check if dependencies are installed:**
```bash
pip3 list | grep -E "torch|stable-baselines3|gymnasium"
```

You should see:
- `torch` (version 2.0 or higher)
- `stable-baselines3` (version 2.2 or higher)
- `gymnasium` (version 0.29 or higher)

**Check logs for errors:**
```bash
sudo tail -100 /var/log/pwnagotchi.log | grep -i error
```

### WiFi Becoming Unstable?

If you experience WiFi instability, you can:

1. **Slow down learning** - Increase the update interval:
```toml
min_update_interval = 60  # Update every 60 seconds instead of 30
```

2. **Reduce parameter changes** - Make changes more gradual:
```toml
max_param_change_rate = 0.2  # 20% max change instead of 30%
```

3. **Disable AI temporarily**:
```toml
enabled = false
```

Then restart: `sudo systemctl restart pwnagotchi`

### Low Performance?

The AI takes time to learn! Give it at least **100 epochs** (several hours) to develop a good strategy.

Watch the reward values in the logs - they should gradually increase over time:
```bash
sudo tail -f /var/log/pwnagotchi.log | grep "REWARD"
```

## Quick Start Configuration

Here's a **conservative** configuration for first-time users:

```toml
[ai]
enabled = true
path = "/root/.pwnagotchi-ai.pt"
verbose = true  # Helpful for monitoring at first
stability_monitoring = true
max_errors_per_minute = 3  # More conservative (default is 5)
min_update_interval = 45  # Slower updates (default is 30)
max_param_change_rate = 0.2  # Smaller changes (default is 0.3)
```

## Disabling the AI

If you want to go back to the original behavior:

1. Edit config:
```bash
sudo nano /etc/pwnagotchi/config.toml
```

2. Change:
```toml
[ai]
enabled = false
```

3. Restart:
```bash
sudo systemctl restart pwnagotchi
```

## More Information

For detailed documentation, see:
- **AI_README.md** - Complete technical documentation
- **pwnagotchi/ai/** - Source code with comments

## Support

If you run into issues:
1. Check the logs: `sudo tail -100 /var/log/pwnagotchi.log`
2. Verify dependencies are installed
3. Try the conservative configuration above
4. Disable AI and report the issue

---

**Happy hunting! 🎯**

The AI will learn to optimize your Pwnagotchi's performance over time. Be patient and let it train for at least a few hours before judging its performance.
