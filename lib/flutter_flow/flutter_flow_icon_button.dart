import 'package:flutter/material.dart';

/// A custom icon button widget for FlutterFlow
class FlutterFlowIconButton extends StatelessWidget {
  final double borderRadius;
  final double buttonSize;
  final Color? fillColor;
  final Widget icon;
  final VoidCallback? onPressed;

  const FlutterFlowIconButton({
    super.key,
    required this.borderRadius,
    required this.buttonSize,
    this.fillColor,
    required this.icon,
    this.onPressed,
  });

  @override
  Widget build(BuildContext context) {
    return Container(
      width: buttonSize,
      height: buttonSize,
      decoration: BoxDecoration(
        color: fillColor,
        borderRadius: BorderRadius.circular(borderRadius),
      ),
      child: IconButton(
        icon: icon,
        onPressed: onPressed,
        padding: EdgeInsets.zero,
      ),
    );
  }
}
