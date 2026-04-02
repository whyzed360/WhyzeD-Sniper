import os
import time

def draw_dashboard():
    # In a real setup, this script would read from your 'gold_bot.log'
    # or ping the MetaApi account.get_streaming_connection()
    
    os.system('clear')
    print("="*40)
    print("      WHYZED EMPIRE: GOLD HEATER V3      ")
    print("="*40)
    print(f" STATUS:    ONLINE")
    print(f" LOCATION:  CENTRAL COMMAND (BAYELSA)")
    print("-"*40)
    print(f" ACCOUNT:   VICTOR MOSES AYAH")
    print(f" BALANCE:   $1,045.20  [+4.52% TODAY]")
    print(f" SHIELD:    ACTIVE (LIMIT: 5%)")
    print("-"*40)
    print(" RECENT LOGS:")
    print(" [21:14] SELL XAUUSD @ 4472.10 - EXECUTED")
    print(" [21:16] MONITORING RSI @ 42.4 (HEATING)")
    print("="*40)
    print(" CTRL+C to Exit Dashboard")

if __name__ == "__main__":
    try:
        while True:
            draw_dashboard()
            time.sleep(5) # Update every 5 seconds
    except KeyboardInterrupt:
        print("\nExiting Command Center...")
