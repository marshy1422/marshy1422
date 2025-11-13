#!/bin/bash

echo "🚀 Viking Wellness Flutter Setup Script"
echo "========================================"
echo ""

# Check if Flutter is installed
if ! command -v flutter &> /dev/null; then
    echo "❌ Flutter is not installed!"
    echo "Please install Flutter first:"
    echo "https://docs.flutter.dev/get-started/install"
    exit 1
fi

echo "✅ Flutter found: $(flutter --version | head -n 1)"
echo ""

# Check Flutter doctor
echo "📋 Running Flutter doctor..."
flutter doctor
echo ""

# Create necessary directories
echo "📁 Creating Flutter project structure..."
mkdir -p android ios web test
echo "✅ Directories created"
echo ""

# Initialize Flutter project (this creates platform-specific files)
echo "🔧 Initializing Flutter project structure..."
flutter create . --org com.vikingwellness --platforms=android,ios --project-name marshy1422 2>&1 | grep -v "already exists"
echo "✅ Flutter project initialized"
echo ""

# Install dependencies
echo "📦 Installing dependencies..."
flutter pub get
echo "✅ Dependencies installed"
echo ""

# Run Flutter analyze to check for issues
echo "🔍 Analyzing code..."
flutter analyze
echo ""

echo "✅ Setup complete!"
echo ""
echo "🎉 Your Viking Wellness app is ready!"
echo ""
echo "To run your app:"
echo "  1. Connect a device or start an emulator"
echo "  2. Run: flutter devices (to see available devices)"
echo "  3. Run: flutter run"
echo ""
echo "Or run in Chrome for quick testing:"
echo "  flutter run -d chrome"
echo ""
