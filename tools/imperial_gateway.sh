#!/bin/bash

# --- WhyzeD Empire: Imperial Gateway ---
# Purpose: System Maintenance & Automation
# ----------------------------------------

clear
echo "=========================================="
echo "      WHYZED EMPIRE: IMPERIAL GATEWAY     "
echo "        ACTION: SYSTEM OPTIMIZATION       "
echo "=========================================="

# 1. Identity Reinforcement
echo -e "\n[1/3] Reinforcing Imperial Identity..."
EMPEROR=$(git config user.name)
if [ -z "$EMPEROR" ]; then
    git config --global user.name "WhyzeD"
    echo " > Identity Restored: WhyzeD"
else
    echo " > Identity Confirmed: $EMPEROR"
fi

# 2. Territory Maintenance (Package Updates)
echo -e "\n[2/3] Scanning for Package Updates..."
pkg update -y && pkg upgrade -y
echo " > All Imperial tools (Clang, Node, Python) are at peak performance."

# 3. Resource Reclamation (Cleaning)
echo -e "\n[3/3] Reclaiming Wasted Territory..."
pkg clean
# Cleaning common build caches often found in Termux/ACode setups
rm -rf ~/.cache/pip
rm -rf ~/.npm/_cacache
echo " > Cache cleared. Storage territory optimized."

echo -e "\n=========================================="
echo "    MAINTENANCE COMPLETE. EMPIRE SECURED. "
echo "=========================================="
