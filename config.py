# config.py
import os
from dotenv import load_dotenv

load_dotenv()  # Load .env automatically

# Telegram / Project
TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
TELEGRAM_ADMIN_ID = os.environ.get("TELEGRAM_ADMIN_ID")
TELEGRAM_CHANNEL_ID = os.environ.get("TELEGRAM_CHANNEL_ID")
PROJECT_NAME = os.environ.get("PROJECT_NAME", "IceGods-TelegramBot")
BRAND_NAME = os.environ.get("BRAND_NAME", "IceGods")
VIP_GROUP = os.environ.get("VIP_GROUP")

# Webhook / Deployment
PORT = int(os.environ.get("PORT", 5000))
WEBHOOK_URL = os.environ.get("WEBHOOK_URL")
HOST = os.environ.get("HOST", "0.0.0.0")

# Database
DATABASE_PATH = os.environ.get("DATABASE_PATH", "subscriptions.db")
DATABASE_URL = os.environ.get("DATABASE_URL", f"sqlite:///{DATABASE_PATH}")

# Wallets (optional)
ETH_MAIN_WALLET = os.environ.get("ETH_MAIN_WALLET")
SOL_MAIN_WALLET = os.environ.get("SOL_MAIN_WALLET")
ETH_BACKUP_WALLET = os.environ.get("ETH_BACKUP_WALLET")
SOL_BACKUP_WALLET = os.environ.get("SOL_BACKUP_WALLET")
BTC_WALLET = os.environ.get("BTC_WALLET")

# API Keys
CMC_API_KEY = os.environ.get("CMC_API_KEY")
ETHERSCAN_API_KEY = os.environ.get("ETHERSCAN_API_KEY")
INFURA_API_KEY = os.environ.get("INFURA_API_KEY")
COINGECKO_API_KEY = os.environ.get("COINGECKO_API_KEY")

# Environment flags
DEBUG = os.environ.get("DEBUG", "False").lower() == "true"
USE_WEBHOOK = os.environ.get("USE_WEBHOOK", "True").lower() == "true"
