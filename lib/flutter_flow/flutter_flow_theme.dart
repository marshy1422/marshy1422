import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

/// FlutterFlow theme configuration
class FlutterFlowTheme {
  static FlutterFlowTheme of(BuildContext context) => FlutterFlowTheme();

  TextStyle get headlineMedium => const TextStyle(
        fontSize: 24,
        fontWeight: FontWeight.w500,
      );

  TextStyle get headlineSmall => const TextStyle(
        fontSize: 20,
        fontWeight: FontWeight.w500,
      );

  TextStyle get titleMedium => const TextStyle(
        fontSize: 18,
        fontWeight: FontWeight.w500,
      );

  TextStyle get bodyMedium => const TextStyle(
        fontSize: 14,
        fontWeight: FontWeight.normal,
      );

  TextStyle get bodySmall => const TextStyle(
        fontSize: 12,
        fontWeight: FontWeight.normal,
      );

  TextStyle get displayLarge => const TextStyle(
        fontSize: 57,
        fontWeight: FontWeight.normal,
      );
}
