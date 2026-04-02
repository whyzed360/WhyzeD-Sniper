#!/bin/bash
echo "ZeDc²: Final Sovereign Polish (Android 14 Optimized)..."

BASE_DIR=$HOME/WHYZED_EMPIRE/ZedLang/app
BIN_DIR=$HOME/WHYZED_EMPIRE/ZedLang/bin
KEYSTORE="$HOME/WHYZED_EMPIRE/apps/whyzedapp/whyzed.keystore"
ALIAS="whyzedkey"

FINAL_APK=$BIN_DIR/ZeDc2_Sovereign.apk
TEMP_APK=$BIN_DIR/temp.apk

mkdir -p $BIN_DIR
rm -f $TEMP_APK $FINAL_APK

echo "ZeDc²: Structuring Sovereign DNA..."
cd $BASE_DIR

# 1. Create a fresh ZIP with ONLY the Manifest first (Stored, not deflated)
zip -0 $TEMP_APK AndroidManifest.xml

# 2. Add the Resource Table and Logic (Stored for speed)
zip -0uj $TEMP_APK resources.arsc classes.dex 2>/dev/null

# 3. Add Assets and Icons
zip -uj $TEMP_APK assets/zed_engine res/drawable/icon.jpg 2>/dev/null

echo "ZeDc²: Aligning to 4-byte boundaries..."
zipalign -f 4 $TEMP_APK $FINAL_APK

echo "ZeDc²: Applying the WhyzeD Imperial Seal..."
apksigner sign --ks $KEYSTORE \
    --ks-key-alias $ALIAS \
    --min-sdk-version 26 \
    --v2-signing-enabled true \
    --v3-signing-enabled true \
    --out $FINAL_APK \
    $FINAL_APK

echo "------------------------------------------------"
echo "ZeDc²: Verification Check..."
apksigner verify -v --min-sdk-version 26 $FINAL_APK
echo "------------------------------------------------"
echo "INSTALL: termux-open $FINAL_APK"
