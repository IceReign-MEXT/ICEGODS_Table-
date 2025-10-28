#!/bin/bash
# 🚀 Force-push all local ICEGODS files to GitHub main branch

echo "🔄 Preparing to push ICEGODS project to GitHub..."

# Ensure we are in the ICEGODS directory
cd ~/ICEGODS || { echo "❌ ICEGODS directory not found!"; exit 1; }

# Initialize git repo if not already
if [ ! -d ".git" ]; then
  git init
  git branch -M main
  git remote add origin https://github.com/IceReign-MEXT/ICEGODS_Table-.git
fi

# Add all files
git add -A

# Commit with timestamp
git commit -m "🔥 Auto push from Termux $(date '+%Y-%m-%d %H:%M:%S')"

# Force push to GitHub
git push -u origin main --force

echo "✅ Push complete! Repository is now live on GitHub."
