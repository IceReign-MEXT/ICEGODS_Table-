#!/data/data/com.termux/files/usr/bin/bash

echo "🔍 Checking and installing ICEGODS dependencies..."

# Activate venv
source venv/bin/activate

# Upgrade pip first
pip install --upgrade pip setuptools wheel

# List of required modules
modules=("flask" "requests" "sqlalchemy" "aiohttp" "web3" "python-telegram-bot" "python-dotenv")

for module in "${modules[@]}"; do
    python3 -c "import $module" 2>/dev/null
    if [ $? -ne 0 ]; then
        echo "⚠️ $module missing → installing..."
        pip install $module
    else
        echo "✅ $module already installed"
    fi
done

# Final test
python3 -c "import flask, requests, sqlalchemy, aiohttp, web3, telegram, dotenv; print('🎯 All modules loaded successfully')"
