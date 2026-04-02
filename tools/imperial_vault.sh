#!/bin/bash

# --- WhyzeD Empire: Imperial Vault ---
# Purpose: Backup & Version Control
# --------------------------------------

echo "=========================================="
echo "        WHYZED EMPIRE: THE VAULT          "
echo "      PROTECTING THE DIGITAL LEGACY       "
echo "=========================================="

# Check if Git is initialized in the Empire
if [ ! -d ".git" ]; then
    echo "[!] Vault not initialized. Initializing now..."
    git init
    echo "Empire Repository Created."
fi

# Status Update
echo -e "\n[SCANNING FOR UNPROTECTED DATA...]"
STATUS=$(git status --short)

if [ -z "$STATUS" ]; then
    echo " > All Imperial data is currently secured."
else
    echo " > Unsecured files detected:"
    echo "$STATUS"
    
    # Prompt for backup (Auto-commit)
    echo -e "\n[!] Securing data now..."
    git add .
    TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")
    git commit -m "Imperial Backup: $TIMESTAMP"
    echo " > Assets locked in the Vault at $TIMESTAMP."
fi

echo -e "\n=========================================="
echo "    THE VAULT IS SEALED AND SECURE.      "
echo "=========================================="
