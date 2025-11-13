import 'package:flutter/material.dart';

/// Model for the Bjorn widget.
/// This handles the state and data for the Viking Wellness pet game.
class BjornModel {
  // Pet stats
  int health = 85;
  int happiness = 92;
  int level = 1;
  int xp = 150;
  int xpNeeded = 200;

  // Evolution stage
  String stage = 'Viking Egg';
  String emoji = '🥚';

  /// Initializes internal state. Called once per instance.
  void initState(BuildContext context) {}

  /// Disposes of any resources used by the model.
  void dispose() {}
}
