#!/data/data/com.termux/files/usr/bin/bash

# --- WHYZED OS: MASTER BUILDER ---
# Identity: Victor Moses Ayah | Alias: WhyzeD

CORE_PATH="$HOME/WHYZED_EMPIRE/Core"
KEYSTORE="$CORE_PATH/empire.keystore"
ALIAS="WhyzeD"

echo -e "\033[1;35m--- WHYZED APP FORGE: ALIAS [WhyzeD] ACTIVE ---\033[0m"

# Prompt for password to unlock the seal
read -s -p "Enter Keystore Password: " PASS
echo ""

function forge_project() {
    local APP_PATH=$1
    local APP_NAME=$2

    if [ -f "$APP_PATH/initial.apk" ]; then
        echo "[*] Signing $APP_NAME with Alias: $ALIAS..."
        apksigner sign --ks "$KEYSTORE" \
                       --ks-pass "pass:$PASS" \
                       --ks-key-alias "$ALIAS" \
                       --out "$APP_PATH/${APP_NAME}_Sovereign.apk" \
                       "$APP_PATH/initial.apk"
        
        if [ $? -eq 0 ]; then
            echo -e "\033[1;32m[SUCCESS] $APP_NAME.apk forged with Imperial Alias.\033[0m"
        else
            echo -e "\033[1;31m[ERROR] Signature failed. Check password or alias.\033[0m"
        fi
    else
        echo "[!] Error: initial.apk not found in $APP_PATH"
    fi
}

# Run Forge for AeonZ project
forge_project "$HOME/WHYZED_EMPIRE/Citadel/AeonZVault" "AeonZ_Vault"
