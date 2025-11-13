import 'package:flutter/material.dart';

/// Button options for FFButtonWidget
class FFButtonOptions {
  final double height;
  final EdgeInsetsGeometry padding;
  final EdgeInsetsGeometry iconPadding;
  final Color? color;
  final TextStyle? textStyle;
  final double elevation;
  final BorderRadius? borderRadius;

  const FFButtonOptions({
    required this.height,
    required this.padding,
    required this.iconPadding,
    this.color,
    this.textStyle,
    required this.elevation,
    this.borderRadius,
  });
}

/// A custom button widget for FlutterFlow
class FFButtonWidget extends StatelessWidget {
  final VoidCallback? onPressed;
  final String text;
  final FFButtonOptions options;

  const FFButtonWidget({
    super.key,
    required this.onPressed,
    required this.text,
    required this.options,
  });

  @override
  Widget build(BuildContext context) {
    return SizedBox(
      height: options.height,
      child: ElevatedButton(
        onPressed: onPressed,
        style: ElevatedButton.styleFrom(
          backgroundColor: options.color,
          elevation: options.elevation,
          padding: options.padding,
          shape: RoundedRectangleBorder(
            borderRadius: options.borderRadius ?? BorderRadius.zero,
          ),
        ),
        child: Text(
          text,
          style: options.textStyle,
        ),
      ),
    );
  }
}
