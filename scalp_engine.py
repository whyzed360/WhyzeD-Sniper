import requests
import time
import random

# --- WHYZED EMPIRE: SCALP CONFIG ---
SYMBOL = "XAUUSD"
LOT = 0.10
TP_PIPS = 10   # Scalping: Tiny profit
SL_PIPS = 20   # 1:2 Ratio
BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"

def send_signal(direction):
    msg = f"WHYZE-D SCALP: {direction} {SYMBOL} \nLot: {LOT} \nTP: {TP_PIPS} \nSL: {SL_PIPS} \n© 2026, WhyzeD Empire."
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={msg}"
    try:
        requests.get(url)
        print(f"[SUCCESS] {direction} Signal Sent to Empire Bridge")
    except:
        print("[ERROR] Bridge Connection Failed")

def start_engine():
    print("--- WHYZED EMPIRE: SCALP ENGINE ACTIVE ---")
    print("© 2026, WhyzeD Empire. Bayelsa State, Nigeria.")
    
    while True:
        # High Frequency: No waiting for big institutions
        direction = random.choice(["BUY", "SELL"])
        send_signal(direction)
        
        # Wait 5 minutes between scalps to see them play out in MT5
        time.sleep(300)

if __name__ == "__main__":
    start_engine()
