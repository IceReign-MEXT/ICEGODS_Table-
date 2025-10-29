#!/bin/bash

echo "--- 🛠️ Starting Comprehensive Termux Build Fix ---"

# 1. Update Termux and Upgrade packages
echo "1. Updating Termux repositories and upgrading packages..."
pkg update -y
pkg upgrade -y

# 2. Install Essential Build Tools and Libraries
# clang, make, pkg-config, and binutils are essential for C/C++ compilation.
echo "2. Installing Core Build Tools (clang, make, binutils, pkg-config)..."
pkg install clang make binutils pkg-config -y

# 3. Install Python Development Headers
# Required for any Python package that links to C libraries (like cryptography)
echo "3. Installing Python Development Headers..."
pkg install python-dev -y

# 4. Install Rust Compiler
# The base Rust package from Termux is the most reliable way to get rustc.
echo "4. Installing Rust Compiler..."
pkg install rust -y

# 5. Reinstall Python Dependencies (Inside venv)
echo "5. Attempting clean installation of Python dependencies..."
# Ensure the virtual environment is sourced
if [ -f venv/bin/activate ]; then
    source venv/bin/activate
fi

# --no-cache-dir forces a fresh build using the newly installed system tools
pip install --no-cache-dir -r requirements.txt

echo "--- ✅ Setup Script Finished ---"
echo "Check output for 'Successfully installed...'"


