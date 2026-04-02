from flask import Flask, render_template_string
import threading
import time
import requests

app = Flask(__name__)

# --- THE BACKGROUND SNIPER LOGIC ---
def imperial_sniper_loop():
    """This runs 24/7 in the cloud, even if nobody is watching the site"""
    while True:
        try:
            # Your trading logic goes here (Scanning Gold, checking filters)
            # For now, it just updates the heart-beat
            with open('status.txt', 'w') as f:
                f.write(f"BULLISH|True|{time.strftime('%H:%M:%S')}")
        except Exception as e:
            print(f"Error in Sniper: {e}")
        time.sleep(60) # Scan every minute

# Start the bot in a separate thread
threading.Thread(target=imperial_sniper_loop, daemon=True).start()

@app.route('/')
def index():
    try:
        with open('status.txt', 'r') as f:
            data = f.read().split('|')
            bias, ready, sync = data[0], data[1], data[2]
    except:
        bias, ready, sync = "SYNCING", "False", "N/A"
    
    scol = "#00ff00" if ready == "True" else "#ff0000"
    
    return render_template_string('''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>WhyzeD Sniper</title>
    <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
    <style>
        body { background: #4a0000; color: #ffb3b3; font-family: sans-serif; text-align: center; padding: 15px; margin: 0; }
        .panel { background: #1a0000; border-radius: 20px; padding: 20px; margin: 15px auto; max-width: 380px; text-align: left; border: 1px solid #600000; }
        .active-text { color: #fff; font-size: 2em; font-weight: bold; margin: 5px 0; }
        .chart-box { background: #1a0000; border-radius: 20px; padding: 10px; margin: 15px auto; max-width: 380px; border: 1px solid #600000; height: 300px; }
        .status-dot { height: 12px; width: 12px; border-radius: 50%; display: inline-block; box-shadow: 0 0 8px {{scol}}; background: {{scol}}; }
    </style>
</head>
<body>
    <h1 style="font-style:italic;">WhyzeD SNIPER</h1>
    <div class="panel">
        <div style="display:flex; justify-content:space-between; align-items:center;">
            <span>BOT STATUS</span><span class="status-dot"></span>
        </div>
        <div class="active-text">ACTIVE</div>
        <div style="font-size:0.85em;">
            Sentinel: <span style="color:white;">{{bias}}</span><br>
            Sync: <span style="color:white;">{{sync}}</span>
        </div>
    </div>
    <div class="chart-box" id="tv_chart"></div>
    <script>
    new TradingView.widget({
      "autosize": true, "symbol": "OANDA:XAUUSD", "interval": "1", "theme": "dark", "container_id": "tv_chart", "backgroundColor": "#1a0000"
    });
    </script>
</body>
</html>
''', bias=bias, ready=ready, sync=sync, scol=scol)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
