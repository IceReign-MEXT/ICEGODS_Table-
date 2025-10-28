#!/usr/bin/env python3
import os
import subprocess
import sys
import sqlite3
import requests
from pathlib import Path
from dotenv import load_dotenv

# ===============================
# CONFIG
# ===============================
ENV_FILE = ".env"
REQUIRED_MODULES = [
    "flask",
    "requests",
    "sqlalchemy",
    "aiohttp",
    "web3",
    "python-telegram-bot",
    "python-dotenv"
]

# ===============================
# LOAD ENV
# ===============================
if not Path(ENV_FILE).exists():
    print(f"❌ {ENV_FILE} missing! Fill it first.")
    sys.exit(1)

load_dotenv(ENV_FILE)

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_ADMIN_ID = os.getenv("TELEGRAM_ADMIN_ID")
TELEGRAM_CHANNEL_ID = os.getenv("TELEGRAM_CHANNEL_ID")
DATABASE_URL = os.getenv("DATABASE_URL")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")
PORT = int(os.getenv("PORT", 5000))

# ===============================
# CHECK VENV
# ===============================
VENV_DIR = "venv"
if not Path(VENV_DIR).exists():
    print("⚠️ Virtual environment not found. Creating...")
    subprocess.run([sys.executable, "-m", "venv", VENV_DIR])
activate_script = Path(VENV_DIR) / "bin" / "activate_this.py"
if activate_script.exists():
    with open(activate_script) as f:
        exec(f.read(), {"__file__": str(activate_script)})

# ===============================
# INSTALL MODULES
# ===============================
for module in REQUIRED_MODULES:
    try:
        __import__(module)
        print(f"✅ Module loaded: {module}")
    except ImportError:
        print(f"⚠️ {module} missing → installing...")
        subprocess.run([sys.executable, "-m", "pip", "install", module])

# ===============================
# CHECK DATABASE
# ===============================
if DATABASE_URL.startswith("sqlite:///"):
    db_path = DATABASE_URL.replace("sqlite:///", "")
    if not Path(db_path).exists():
        print(f"⚠️ Database not found → creating {db_path}")
        conn = sqlite3.connect(db_path)
        conn.close()
    print(f"✅ Database ready → {db_path}")

# ===============================
# CHECK ENV VARS
# ===============================
missing_env = []
for key in ["TELEGRAM_BOT_TOKEN", "TELEGRAM_ADMIN_ID", "TELEGRAM_CHANNEL_ID", "DATABASE_URL", "WEBHOOK_URL"]:
    if not os.getenv(key):
        missing_env.append(key)
if missing_env:
    print(f"❌ Missing env vars: {missing_env}")
else:
    print("✅ All required env vars detected.")

# ===============================
# CHECK INTERNET
# ===============================
try:
    requests.get("https://api.telegram.org", timeout=5)
    print("✅ Internet connection OK")
except Exception:
    print("❌ No internet connection!")

# ===============================
# CHECK TELEGRAM BOT
# ===============================
try:
    from telegram import Bot
    bot = Bot(token=TELEGRAM_BOT_TOKEN)
    me = bot.get_me()
    print(f"✅ Telegram bot connected → @{me.username}")
except Exception as e:
    print(f"❌ Telegram bot connection failed: {e}")

# ===============================
# CHECK WEBHOOK
# ===============================
if WEBHOOK_URL:
    try:
        r = requests.get(WEBHOOK_URL, timeout=5)
        print(f"🌐 Webhook reachable → {WEBHOOK_URL} [Status: {r.status_code}]")
    except Exception as e:
        print(f"❌ Webhook unreachable → {WEBHOOK_URL} | {e}")

# ===============================
# START BOT
# ===============================
print("🚀 Starting bot...")
subprocess.run([sys.executable, "start_icegods.py"])
