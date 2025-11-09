"""
Feature extraction for Pwnagotchi AI
Converts state information into observation vectors for the neural network
"""
import numpy as np
import pwnagotchi.mesh.wifi as wifi

MAX_EPOCH_DURATION = 1024


def describe(extended=False):
    """
    Returns the feature space dimensions

    Args:
        extended: Whether to use extended channel range (5GHz)

    Returns:
        (histogram_size, observation_shape) tuple
    """
    if not extended:
        histogram_size = wifi.NumChannels
    else:
        # Extended spectrum for 5GHz support
        histogram_size = wifi.NumChannelsExt

    # Feature vector size calculation:
    # - AP histogram per channel (histogram_size)
    # - Client histogram per channel (histogram_size)
    # - Peer histogram per channel (histogram_size)
    # - Epoch duration (1)
    # - Inactive epochs ratio (1)
    # - Active epochs ratio (1)
    # - Missed interactions ratio (1)
    # - Channel hops ratio (1)
    # - Deauths ratio (1)
    # - Associations ratio (1)
    # - Handshakes ratio (1)
    observation_size = (histogram_size * 3) + 8

    return histogram_size, (observation_size,)


def featurize(state, step):
    """
    Convert state dictionary to feature vector

    Args:
        state: Dictionary containing epoch state information
        step: Current epoch number

    Returns:
        Normalized numpy array of features
    """
    # Avoid division by zero
    tot_epochs = step + 1e-10
    tot_interactions = (state['num_deauths'] + state['num_associations']) + 1e-10

    # Concatenate all features into single vector
    features = np.concatenate((
        # WiFi environment features (normalized histograms)
        state['aps_histogram'],
        state['sta_histogram'],
        state['peers_histogram'],

        # Temporal features
        [np.clip(state['duration_secs'] / MAX_EPOCH_DURATION, 0.0, 1.0)],
        [state['inactive_for_epochs'] / tot_epochs],
        [state['active_for_epochs'] / tot_epochs],

        # Performance features
        [state['missed_interactions'] / tot_interactions],
        [state['num_hops'] / wifi.NumChannels],
        [state['num_deauths'] / tot_interactions],
        [state['num_associations'] / tot_interactions],
        [state['num_handshakes'] / tot_interactions],
    ))

    return features.astype(np.float32)
