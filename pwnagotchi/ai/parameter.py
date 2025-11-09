"""
Parameter management for Pwnagotchi AI
Defines tunable parameters for reinforcement learning
"""


class Parameter:
    """Represents a tunable parameter for the AI"""

    def __init__(self, name, min_value, max_value, meta=None, trainable=True):
        self.name = name
        self.min_value = min_value
        self.max_value = max_value
        self.meta = meta
        self.trainable = trainable

    def space_size(self):
        """Returns the discrete action space size for this parameter"""
        # Use 10 discrete values for each parameter
        # This balances exploration with computational efficiency
        return 10

    def to_param_value(self, action):
        """
        Convert discrete action (0-9) to actual parameter value

        Args:
            action: Integer from 0 to space_size()-1

        Returns:
            Actual parameter value in [min_value, max_value]
        """
        # Map action index to value in parameter range
        if action == 0:
            # Special case for boolean/off state
            return 0 if self.name.startswith('_channel') else self.min_value

        normalized = action / (self.space_size() - 1)
        value = self.min_value + (self.max_value - self.min_value) * normalized

        # Return integer values for integer parameters
        if isinstance(self.min_value, int) and isinstance(self.max_value, int):
            return int(round(value))

        return value

    def __repr__(self):
        return f"Parameter({self.name}, [{self.min_value}, {self.max_value}])"
