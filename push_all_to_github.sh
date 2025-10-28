#!/bin/bash
# 🚀 Safe GitHub Push Script for ICEGODS Project
# Pushes everything except sensitive .env file

echo "🔄 Preparing to push ICEGODS project to GitHub..."

# Move into project directory
cd ~/ICEGODS || { echo "❌ ICEGODS directory not found!"; exit 1; }

# Initialize git if not done
if [ ! -d ".git" ]; then
  echo "📦 Initializing new Git repository..."
  git init
  git branch -M main
  git remote add origin https://github.com/IceReign-MEXT/ICEGODS_Table-.git
fi

# Create .gitignore if missing
if [ ! -f ".gitignore" ]; then
  echo "🧹 Creating .gitignore..."
  cat <<EOF > .gitignore
# Ignore sensitive or unnecessary files
.env
__pycache__/
*.log
*.db
venv/
.DS_Store
*.pyc
EOF
fi

# Add everything except ignored files
git add -A

# Commit with auto timestamp
git commit -m "🔥 Auto push from Termux $(date '+%Y-%m-%d %H:%M:%S')"

# Push changes forcibly to main branch
git push -u origin main --force

echo "✅ Push complete!"
echo "🌐 Check your repo: https://github.com/IceReign-MEXT/ICEGODS_Table-"
