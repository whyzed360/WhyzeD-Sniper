#!/bin/bash
clear
echo "=========================================="
echo "    WHYZED EMPIRE: CENTRAL COMMAND       "
echo "=========================================="
echo " DATE: $(date)"
echo " STATUS: SOVEREIGN"
echo " ENGINE: $(expo --version 2>/dev/null || echo 'Expo Ready')"
echo " PROJECTS: $(ls ~/WHYZED_EMPIRE/apps | wc -l)"
echo "=========================================="
echo " Welcome, Emperor. Your tools are online. "
