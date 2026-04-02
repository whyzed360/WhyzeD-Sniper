import asyncio
import pandas as pd
import pandas_ta as ta
from metaapi_cloud_sdk import MetaApi

# --- CREDENTIALS ---
# Replace with your actual MetaApi Token from app.metaapi.cloud/token
TOKEN = 'YOUR_METAAPI_TOKEN'
# Replace with the Account ID from the MetaApi "Accounts" tab (looks like a UUID)
ACCOUNT_ID = 'YOUR_METAAPI_ACCOUNT_ID'

# --- MICRO-ACCOUNT CONFIG (FOR $9 BALANCE) ---
LOT_SIZE = 0.01       
RISK_USD = 1.0        
GAIN_USD = 3.0        
MAGIC_NUMBER = 555777

async def run_bot():
    api = MetaApi(TOKEN)
    try:
        # Note: MetaApi requires the Account ID from THEIR dashboard
        account = await api.metatrader_account_api.get_account(ACCOUNT_ID)
        conn = await account.get_streaming_connection()
        await conn.connect()
        await conn.wait_synchronized()
        
        print(f"WHYZED EMPIRE: Micro-Uplink Online. Balance: $9.00 Strategy: 1:3")

        while True:
            candles = await conn.get_history('XAUUSD', '15m', 100)
            df = pd.DataFrame(candles)
            
            rsi = ta.rsi(df['close'], length=14).iloc[-1]
            ema = ta.ema(df['close'], length=50).iloc[-1]
            price = df['close'].iloc[-1]

            positions = conn.terminal_state.positions
            if len(positions) > 0:
                await asyncio.sleep(60)
                continue

            # BUY SIGNAL
            if price > ema and rsi > 55:
                sl = round(price - 1.0, 2)
                tp = round(price + 3.0, 2)
                print(f"BUY EXECUTED: Price {price} | SL {sl} | TP {tp}")
                await conn.create_order('XAUUSD', 'ORDER_TYPE_BUY', LOT_SIZE, price, sl, tp, {'magic': MAGIC_NUMBER})
                await asyncio.sleep(600)

            # SELL SIGNAL
            elif price < ema and rsi < 45:
                sl = round(price + 1.0, 2)
                tp = round(price - 3.0, 2)
                print(f"SELL EXECUTED: Price {price} | SL {sl} | TP {tp}")
                await conn.create_order('XAUUSD', 'ORDER_TYPE_SELL', LOT_SIZE, price, sl, tp, {'magic': MAGIC_NUMBER})
                await asyncio.sleep(600)

            await asyncio.sleep(30)

    except Exception as e:
        print(f"CRITICAL SYSTEM ERROR: {e}")

if __name__ == "__main__":
    asyncio.run(run_bot())
