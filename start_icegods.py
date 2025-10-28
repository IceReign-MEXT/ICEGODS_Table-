#!/usr/bin/env python3
# start_icegods.py
import asyncio
import os
from dotenv import load_dotenv
from telegram import Bot
from telegram.error import TelegramError
from flask import Flask, request

# Load .env
load_dotenv()

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
WEBHOOK_URL = os.environ.get("WEBHOOK_URL")
PORT = int(os.environ.get("PORT", 5000))
HOST = os.environ.get("HOST", "0.0.0.0")

if not TOKEN:
    print("❌ TELEGRAM_BOT_TOKEN not set in .env")
    exit(1)

bot = Bot(token=TOKEN)

# Flask app for webhook
app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    update = request.get_json()
    # You can handle updates here or pass to Dispatcher
    print("🔔 Incoming update:", update)
    return "OK", 200

async def start_bot():
    try:
        me = await bot.get_me()
        print(f"✅ Bot connected: @{me.username}")
    except TelegramError as e:
        print("❌ Telegram bot connection failed:", e)
        return

    if WEBHOOK_URL:
        try:
            await bot.set_webhook(WEBHOOK_URL)
            print(f"🌐 Webhook set to {WEBHOOK_URL}")
        except TelegramError as e:
            print("⚠️ Failed to set webhook:", e)
    else:
        print("⚠️ WEBHOOK_URL missing in .env")

    # Start Flask app
    print(f"🚀 Starting Flask server on {HOST}:{PORT}")
    app.run(host=HOST, port=PORT)

if __name__ == "__main__":
    asyncio.run(start_bot())
