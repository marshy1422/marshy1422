import 'package:flutter/material.dart';
import 'pages/bjorn/bjorn_widget.dart';

void main() {
  runApp(const VikingWellnessApp());
}

class VikingWellnessApp extends StatelessWidget {
  const VikingWellnessApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Viking Wellness',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        brightness: Brightness.dark,
        primaryColor: const Color(0xFFED8936),
        scaffoldBackgroundColor: const Color(0xFF1A1F2E),
        useMaterial3: true,
      ),
      home: const BjornWidget(),
    );
  }
}
