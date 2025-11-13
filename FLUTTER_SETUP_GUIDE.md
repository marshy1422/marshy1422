# 🚀 How to Get Your Viking Wellness Flutter App Working

This guide will help you set up and run your Flutter mobile app.

---

## 📋 Prerequisites

Before you start, you need to install:

### 1. **Flutter SDK**
```bash
# macOS/Linux
git clone https://github.com/flutter/flutter.git -b stable
export PATH="$PATH:`pwd`/flutter/bin"

# Windows - Download from:
# https://docs.flutter.dev/get-started/install/windows
```

### 2. **Verify Installation**
```bash
flutter doctor
```
This will show what you need to install (Android Studio, Xcode, etc.)

---

## 🏗️ Option 1: Convert This Repository to Flutter Project

### Step 1: Add Missing Flutter Files

Run these commands in your project root:

```bash
# Create required Flutter directories
mkdir -p android ios web test

# Create main.dart entry point
cat > lib/main.dart << 'EOF'
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
      theme: ThemeData(
        brightness: Brightness.dark,
        primarySwatch: Colors.orange,
      ),
      home: const BjornWidget(),
    );
  }
}
EOF

# Initialize Flutter project structure
flutter create . --org com.vikingwellness --platforms=android,ios
```

### Step 2: Install Dependencies
```bash
flutter pub get
```

### Step 3: Run the App
```bash
# On Android emulator/device
flutter run

# On iOS simulator (macOS only)
flutter run -d "iPhone 15"

# On Chrome (for testing)
flutter run -d chrome
```

---

## 🆕 Option 2: Create a New Flutter Project (Recommended)

### Step 1: Create New Project
```bash
# Navigate to where you want the project
cd ~/Projects  # or wherever you keep projects

# Create new Flutter project
flutter create viking_wellness --org com.vikingwellness

cd viking_wellness
```

### Step 2: Copy Your Fixed Files
```bash
# Copy the lib directory from your current repo
cp -r /path/to/marshy1422/lib/* lib/

# Copy pubspec.yaml
cp /path/to/marshy1422/pubspec.yaml .
```

### Step 3: Update `lib/main.dart`
```dart
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
      ),
      home: const BjornWidget(),
    );
  }
}
```

### Step 4: Install Dependencies
```bash
flutter pub get
```

### Step 5: Run the App
```bash
# List available devices
flutter devices

# Run on specific device
flutter run
```

---

## 📱 Running on Physical Devices

### Android
1. Enable Developer Mode on your phone:
   - Go to Settings > About Phone
   - Tap "Build Number" 7 times
2. Enable USB Debugging:
   - Settings > Developer Options > USB Debugging
3. Connect phone via USB
4. Run: `flutter run`

### iOS (macOS only)
1. Connect iPhone via USB
2. Trust the computer on your iPhone
3. Open `ios/Runner.xcworkspace` in Xcode
4. Sign the app with your Apple ID
5. Run: `flutter run`

---

## 🔧 Fixing Common Issues

### Issue: "Package not found"
**Solution:** Make sure package name matches in:
- `pubspec.yaml` (name: marshy1422)
- Import statements (`package:marshy1422/...`)

### Issue: "Google Fonts error"
**Solution:** Add internet permission

**Android:** `android/app/src/main/AndroidManifest.xml`
```xml
<uses-permission android:name="android.permission.INTERNET"/>
```

**iOS:** Already enabled by default

### Issue: "Undefined class 'BjornModel'"
**Solution:** The import path might be wrong. Check:
```dart
import 'bjorn_model.dart';  // Should be relative
```

---

## 🎨 Next Steps: Making It Functional

### 1. Add Navigation
Create additional pages for:
- AI Chat screen
- Mood Tracking screen
- Journal screen
- CBT Exercises screen

### 2. Add State Management
Update `bjorn_model.dart` to use ChangeNotifier:
```dart
import 'package:flutter/material.dart';

class BjornModel extends ChangeNotifier {
  int _health = 85;
  int _happiness = 92;
  int _xp = 150;

  int get health => _health;
  int get happiness => _happiness;
  int get xp => _xp;

  void feedBjorn() {
    _health = (_health + 10).clamp(0, 100);
    _happiness = (_happiness + 5).clamp(0, 100);
    notifyListeners();
  }

  void playWithBjorn() {
    _happiness = (_happiness + 10).clamp(0, 100);
    notifyListeners();
  }
}
```

### 3. Wire Up Buttons
In `bjorn_widget.dart`, replace `print()` statements:
```dart
FFButtonWidget(
  onPressed: () {
    _model.feedBjorn();
    setState(() {});
  },
  text: '🍖 Feed',
  // ...
)
```

### 4. Add Real Data Storage
Use packages like:
- `shared_preferences` - Simple key-value storage
- `sqflite` - SQLite database
- `hive` - Fast NoSQL database

---

## 📚 Learning Resources

- [Flutter Official Docs](https://docs.flutter.dev/)
- [Flutter Cookbook](https://docs.flutter.dev/cookbook)
- [Dart Language Tour](https://dart.dev/guides/language/language-tour)
- [Flutter YouTube Channel](https://www.youtube.com/c/flutterdev)

---

## 🐛 Still Not Working?

1. **Check Flutter version:**
   ```bash
   flutter --version
   ```
   Should be 3.0.0 or higher

2. **Clean and rebuild:**
   ```bash
   flutter clean
   flutter pub get
   flutter run
   ```

3. **Check for errors:**
   ```bash
   flutter analyze
   ```

4. **Update packages:**
   ```bash
   flutter pub upgrade
   ```

---

## 📂 Final Project Structure

```
viking_wellness/
├── android/              # Android-specific files
├── ios/                  # iOS-specific files
├── lib/
│   ├── main.dart        # Entry point
│   ├── flutter_flow/    # FlutterFlow helpers
│   └── pages/
│       └── bjorn/
│           ├── bjorn_widget.dart
│           └── bjorn_model.dart
├── test/                # Tests
├── pubspec.yaml        # Dependencies
└── README.md           # Your project docs
```

---

## ✅ Quick Start Command Summary

```bash
# 1. Create project
flutter create viking_wellness
cd viking_wellness

# 2. Copy your files
cp -r /path/to/lib/* lib/
cp /path/to/pubspec.yaml .

# 3. Get dependencies
flutter pub get

# 4. Run app
flutter run
```

That's it! Your Viking Wellness app should now be running! 🎉
