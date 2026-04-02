#!/bin/bash
clear
echo "=========================================="
echo "      WHYZED EMPIRE: CENTRAL COMMAND      "
echo "        STATUS: ACTIVE | ROLE: EMPEROR    "
echo "        IDENTITY: $(git config user.name) "
echo "=========================================="

DATE=$(date)
UPTIME=$(uptime -p)
STORAGE=$(df -h . | awk 'NR==2 {print $4}')

echo -e "\n[LOG] Imperial Time: $DATE"
echo "[LOG] System Uptime: $UPTIME"
echo "[LOG] Available Territory (Storage): $STORAGE"

echo -e "\n[SCANNING SUB-DOMAINS...]"
for dir in */; do
    if [ -d "$dir" ] && [[ "$dir" != "."* ]]; then
        echo " > Territory Identified: ${dir%/}"
    fi
done

echo -e "\n=========================================="
echo "   GLORY TO THE EMPIRE. STANDING BY...    "
echo "=========================================="
