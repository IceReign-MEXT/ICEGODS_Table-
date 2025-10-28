#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import importlib
import sqlite3
import requests
from dotenv import load_dotenv

# ===============================
# Load environment
# ===============================
load_dotenv()

REQUIRED_ENV_VARS = [
    "TELEGRAM_BOT_TOKEN",
    "TELEGRAM_ADMIN_ID",
    "TELEGRAM_CHANNEL_ID",
    "DATABASE_URL",
    "WEBHOOK_URL"
]

REQUIRED_MODULES = [
    "flask",
    "requests",
    "sqlalchemy",
    "aiohttp",
    "web3",
    "telegram",
    "dotenv"
]

print("🔍 ICEGODS BOT DEPLOYMENT CHECK\n")

# ===============================
# Check environment variables
# ===============================
print("🌿 Checking environment variables...")
for var in REQUIRED_ENV_VARS:
    if os.getenv(var):
        print(f"✅ {var} detected")
    else:
        print(f"❌ {var} missing")

# ===============================
# Check Python modules
# ===============================
print("\n📦 Checking Python modules...")
for module in REQUIRED_MODULES:
    try:
        importlib.import_module(module)
        print(f"✅ Module loaded: {module}")
    except ModuleNotFoundError:
        print(f"❌ Missing module: {module}")

# ===============================
# Check database
# ===============================
print("\n💾 Checking database...")
db_url = os.getenv("DATABASE_URL")
if db_url and db_url.startswith("sqlite:///"):
    db_path = db_url.replace("sqlite:///", "")
    if os.path.isfile(db_path):
        print(f"✅ Database ready → {db_url}")
    else:
        print(f"❌ Database file missing → {db_path}")
else:
    print(f"⚠️ DATABASE_URL not set or invalid")

# ===============================
# Check webhook URL
# ===============================
webhook = os.getenv("WEBHOOK_URL")
if webhook:
    try:
        resp = requests.head(webhook, timeout=5)
        print(f"🌐 Webhook reachable → {webhook} [Status: {resp.status_code}]")
    except Exception as e:
        print(f"❌ Webhook unreachable → {webhook} | Error: {e}")
else:
    print("❌ Webhook URL not set")

# ===============================
# Check internet connection
# ===============================
print("\n🔌 Checking internet connectivity...")
try:
    requests.get("https://api.telegram.org", timeout=5)
    print("✅ Internet connection OK")
except Exception:
    print("❌ Internet connection FAILED")

# ===============================
# Telegram token basic check
# ===============================
bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
if bot_token:
    print("✅ TELEGRAM_BOT_TOKEN detected (cannot validate fully without running bot)")
else:
    print("❌ TELEGRAM_BOT_TOKEN missing")

print("\n🧩 DEPLOYMENT CHECK COMPLETE.")
