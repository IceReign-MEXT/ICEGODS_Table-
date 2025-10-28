# ===========================
# ICEGODS Bot Dockerfile
# Deployable on Render / Fly.io / Docker Hub
# ===========================

# Use official lightweight Python image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential curl libssl-dev libffi-dev python3-dev git \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip install --upgrade pip setuptools wheel

# Install Python dependencies
RUN pip install --no-cache-dir flask requests sqlalchemy aiohttp web3 python-telegram-bot python-dotenv

# Optional: install any extras from requirements.txt
COPY requirements.txt .
RUN if [ -f "requirements.txt" ]; then pip install -r requirements.txt; fi

# Copy environment variables
COPY .env /app/.env

# Expose Flask/webhook port
EXPOSE 5000

# Default environment
ENV PYTHONUNBUFFERED=1
ENV PORT=5000

# Start command
CMD ["python3", "start_icegods.py"]
