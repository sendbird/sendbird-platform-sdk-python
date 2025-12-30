#!/bin/bash

# Sendbird Platform SDK Python Build Script
# This script builds the Python SDK package in multiple formats

set -e  # Exit on error

echo "================================================"
echo "Sendbird Platform SDK Python - Build Script"
echo "================================================"
echo ""

# Get the directory where the script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

# Clean previous builds
echo "🧹 Cleaning previous build artifacts..."
rm -rf build/
rm -rf dist/
rm -rf *.egg-info
echo "✅ Cleanup completed"
echo ""

# Build source distribution and wheel
echo "🔨 Building source distribution and wheel..."
python3 setup.py sdist bdist_wheel
echo "✅ Source distribution and wheel built"
echo ""

# Build egg distribution
echo "🥚 Building egg distribution..."
python3 setup.py bdist_egg
echo "✅ Egg distribution built"
echo ""

# Display build results
echo "================================================"
echo "📦 Build completed successfully!"
echo "================================================"
echo ""
echo "Generated packages in dist/:"
ls -lh dist/
echo ""
echo "Build artifacts:"
for file in dist/*; do
    if [ -f "$file" ]; then
        size=$(ls -lh "$file" | awk '{print $5}')
        filename=$(basename "$file")
        echo "  - $filename ($size)"
    fi
done
echo ""
echo "✨ All builds completed successfully!"

