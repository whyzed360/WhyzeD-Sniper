#!/data/data/com.termux/files/usr/bin/bash

# You must have 'aapt2', 'openjdk-17', and 'android-tools' installed
echo "[*] Compiling Resources..."
aapt2 compile --dir res -o compiled_res.flata
aapt2 link --manifest AndroidManifest.xml -I $PREFIX/share/java/android.jar --java src --flat-files compiled_res.flata -o initial.apk

echo "[*] Compiling Java Source..."
javac -d obj -cp $PREFIX/share/java/android.jar src/empire/whyzed/aeonz/MainActivity.java

echo "[*] Converting to Dex (The Android Execution Format)..."
d8 --release --output bin/ --lib $PREFIX/share/java/android.jar obj/empire/whyzed/aeonz/*.class

echo "[*] Adding Dex to APK..."
zip -uj initial.apk bin/classes.dex

echo "[*] Signing the Imperial APK..."
# Create a temporary key if not exists
if [ ! -f "empire.keystore" ]; then
    keytool -genkey -v -keystore empire.keystore -alias whyzed -keyalg RSA -keysize 2048 -validity 10000 -storepass whyzedpass -keypass whyzedpass -dname "CN=WhyzeD, O=Empire, C=NG"
fi
apksigner sign --ks empire.keystore --ks-pass pass:whyzedpass initial.apk

mv initial.apk AeonZ_Final.apk
echo "[+] Imperial APK 'AeonZ_Final.apk' is ready for installation."
