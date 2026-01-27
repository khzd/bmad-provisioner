#!/bin/bash
# BMAD Provisioner - Quick Install Script

set -e

echo "🚀 Installing BMAD Provisioner..."

# Check Python version
python_version=$(python3 --version 2>&1 | awk '{print $2}' | cut -d. -f1,2)
echo "✅ Python version: $python_version"

# Create virtual environment
if [ ! -d "venv-bp" ]; then
    echo "📦 Creating virtual environment venv-bp..."
    python3 -m venv venv-bp
fi

# Activate venv
echo "✅ Activating virtual environment..."
source venv-bp/bin/activate

# Install dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt

# Make executable
chmod +x bmad_provisioner.py

echo ""
echo "✅ Installation complete!"
echo ""
echo "To use BMAD Provisioner:"
echo "  1. Activate venv: source venv-bp/bin/activate"
echo "  2. Create skills-manifest.yaml (see templates/skills-manifest-healthai.yaml)"
echo "  3. Run: python bmad_provisioner.py --config skills-manifest.yaml --mode analyze"
echo ""
echo "Or use the wrapper: ./run.sh analyze skills-manifest.yaml"
echo ""
echo "Examples in README.md"

