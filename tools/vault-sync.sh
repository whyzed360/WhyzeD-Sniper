#!/bin/bash
# --- WHYZED EMPIRE: VAULT SYNC v1 ---

TIMESTAMP=$(date +%Y%m%d)
BACKUP_FILE="WHYZED_EMPIRE_BACKUP_${TIMESTAMP}.tar.gz"

echo -e "\033[1;34m[VAULT]\033[0m Compressing the Empire..."
# We exclude node_modules to keep the backup fast and light
tar --exclude='node_modules' -czf ~/$BACKUP_FILE -C ~ WHYZED_EMPIRE

echo -e "\033[1;32m[VAULT]\033[0m Uploading to Google Drive..."
rclone copy ~/$BACKUP_FILE google_drive:WHYZED_BACKUPS/

echo -e "\033[1;32m[SUCCESS]\033[0m Backup $BACKUP_FILE is secure in the cloud."

# Clean up the local zip to save space on your phone
rm ~/$BACKUP_FILE
