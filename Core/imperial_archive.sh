#!/data/data/com.termux/files/usr/bin/bash

# Imperial Archive Sync Protocol
echo -e "\033[1;34m[ARCHIVE]\033[0m Commencing Imperial Synchronization..."

cd ~/WHYZED_EMPIRE
git add .
git commit -m "Imperial Update: $(date)"

# Replace with your actual GitHub repo URL
# git push origin main

echo -e "\033[1;32m[SUCCESS]\033[0m Archive updated."
