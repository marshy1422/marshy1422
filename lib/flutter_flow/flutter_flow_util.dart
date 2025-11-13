import 'package:flutter/material.dart';

/// Utility function to create a model
T createModel<T>(BuildContext context, T Function() builder) {
  return builder();
}

/// Extension to add divide functionality to lists of widgets
extension ListDivideExt on List<Widget> {
  List<Widget> divide(Widget separator) {
    if (isEmpty) return this;

    final result = <Widget>[];
    for (int i = 0; i < length; i++) {
      result.add(this[i]);
      if (i < length - 1) {
        result.add(separator);
      }
    }
    return result;
  }

  List<Widget> addToStart(Widget widget) {
    return [widget, ...this];
  }

  List<Widget> addToEnd(Widget widget) {
    return [...this, widget];
  }
}
