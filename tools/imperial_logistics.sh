#!/bin/bash

# --- WhyzeD Empire: Imperial Logistics ---
# Purpose: Folder Organization & Cleanliness
# ------------------------------------------

clear
echo "=========================================="
echo "     WHYZED EMPIRE: LOGISTICAL CORE       "
echo "       ORGANIZING IMPERIAL ASSETS         "
echo "=========================================="

# 1. Moving Management Scripts to Tools
echo "[LOG] Relocating command modules to /tools..."
mv central_command.sh tools/ 2>/dev/null
mv imperial_vault.sh tools/ 2>/dev/null
mv imperial_gateway.sh tools/ 2>/dev/null

# 2. Creating Imperial Shortcuts (Aliases)
# This allows you to just type 'empire' to see your command center
echo "[LOG] Creating Imperial Shortcuts..."
BASHRC=~/.bashrc
if ! grep -q "alias empire=" "$BASHRC"; then
    echo "alias empire='~/WHYZED_EMPIRE/tools/central_command.sh'" >> "$BASHRC"
    echo "alias vault='~/WHYZED_EMPIRE/tools/imperial_vault.sh'" >> "$BASHRC"
    echo "alias gateway='~/WHYZED_EMPIRE/tools/imperial_gateway.sh'" >> "$BASHRC"
    source "$BASHRC"
    echo " > Shortcuts 'empire', 'vault', and 'gateway' created."
else
    echo " > Shortcuts already exist."
fi

# 3. Final Scan
echo -e "\n[STATUS] Root directory cleaned."
echo "[STATUS] All systems relocated to ~/WHYZED_EMPIRE/tools/"

echo -e "\n=========================================="
echo "    LOGISTICS COMPLETE. ORDER RESTORED.   "
echo "=========================================="
