#!/bin/bash
# --- WHYZE_D STREAMCAST ENGINE (CLEAN RELAY EDITION) ---

# Load Imperial Config
source "$HOME/WHYZED_EMPIRE/Core/branding/stream_config.env"

SOURCE_URL=$1

if [ -z "$SOURCE_URL" ]; then
    echo -e "\033[1;31m[ERROR]\033[0m No Source URL provided."
    exit 1
fi

echo -e "\033[1;32m[SYSTEM]\033[0m Launching Clean Relay (No Watermark)..."

# RECONNECT LOOP
while true; do
  echo -e "\033[1;33m[UPLINK]\033[0m Relaying clean signal to handles..."
  
  # Removed logo input and filter_complex for a direct, clean relay
  ./ffmpeg -re -i "$SOURCE_URL" \
    -c:v libx264 -preset veryfast -b:v 2500k -maxrate 2500k -bufsize 5000k \
    -c:a aac -b:a 128k -ar 44100 \
    -f flv "$YT_STREAM_URL$YT_STREAM_KEY" \
    -f flv "$FB_STREAM_URL$FB_STREAM_KEY"

  echo -e "\033[1;31m[ALERT]\033[0m Connection lost. Reconnecting in 5 seconds..."
  sleep 5
done
