#!/bin/bash
# --- WHYZED EMPIRE: APP FORGE v1 ---

APP_NAME=$1
TARGET_DIR="$HOME/WHYZED_EMPIRE/apps/$APP_NAME"

if [ -z "$APP_NAME" ]; then
    echo "Usage: forge-app [AppName]"
    exit 1
fi

echo -e "\033[1;34m[FORGE]\033[0m Initializing $APP_NAME..."

# Check if Core Tools are linked
if [[ ":$PATH:" != *":$HOME/WHYZED_EMPIRE/tools:"* ]]; then
    export PATH="$HOME/WHYZED_EMPIRE/tools:$PATH"
fi

# Create directory
mkdir -p "$TARGET_DIR"
cd "$TARGET_DIR"

# Check for Node/Expo - Use existing cache if available
if [ -d "$HOME/WHYZED_EMPIRE/Library/node_modules_cache/node_modules" ]; then
    echo -e "\033[1;32m[CACHE]\033[0m Linking existing Imperial Modules..."
    ln -s "$HOME/WHYZED_EMPIRE/Library/node_modules_cache/node_modules" .
else
    echo -e "\033[1;33m[INSTALL]\033[0m First-time setup for modules..."
    npx create-expo-app . --template blank --yes
fi

echo -e "\033[1;32m[SUCCESS]\033[0m $APP_NAME is ready using existing Imperial Tools."
