#!/bin/bash
# BMAD Provisioner - Wrapper script with automatic venv activation

# Activate venv if exists
if [ -d "venv-bp" ]; then
    source venv-bp/bin/activate
else
    echo "⚠️  venv-bp not found. Run: bash install.sh"
    exit 1
fi

# Run provisioner
python bmad_provisioner.py "$@"
