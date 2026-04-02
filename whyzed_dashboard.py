from flask import Flask, render_template_string
import os
import random

app = Flask(__name__)

@app.route('/')
def home():
    # TEST LOGIC: Lowering threshold to 70% to force action on Demo
    accuracy_val = 70.0
    
    # Simple logic to flip bias from Neutral to Bull/Bear more often
    bias_options = ["BULLISH", "BEARISH", "NEUTRAL"]
    # 80% chance to be active, 20% to stay neutral
    current_bias = random.choices(bias_options, weights=[40, 40, 20])[0]
    
    html_template = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>WHYZED SNIPER | IMPERIAL HUB</title>
        <style>
            :root {{
                --bg-imperial: #3b0101;
                --card-void: #0a0000;
                --neon-green: #00ff41;
                --blood-red: #ff3131;
            }}
            body {{ background-color: var(--bg-imperial); color: #fff; font-family: sans-serif; text-align: center; padding: 15px; margin: 0; }}
            .card {{ background: var(--card-void); border-radius: 20px; padding: 20px; margin-bottom: 15px; box-shadow: 0 10px 30px #000; max-width: 400px; margin-left: auto; margin-right: auto; }}
            .green {{ color: var(--neon-green); font-weight: bold; }}
            .red-dot {{ width: 12px; height: 12px; background: var(--blood-red); border-radius: 50%; display: inline-block; box-shadow: 0 0 10px var(--blood-red); }}
            .terminal {{ background: #000; padding: 15px; border-radius: 15px; font-family: monospace; font-size: 0.8rem; text-align: left; border: 1px solid #111; max-width: 370px; margin: 0 auto; }}
        </style>
    </head>
    <body>
        <h1 style="font-style: italic; margin: 0;">WHYZED SNIPER</h1>
        <p style="font-size: 0.7rem; color: #888; margin-bottom: 20px;">IMPERIAL EXECUTION HUB</p>

        <div class="card">
            <div style="display: flex; justify-content: space-between; align-items: flex-start;">
                <div style="text-align: left;"><small style="color: #666">BOT STATUS</small><h2 style="font-size: 2.2rem; margin: 0;">ACTIVE</h2></div>
                <div class="red-dot"></div>
            </div>
            <div style="display: grid; grid-template-columns: 1fr 1fr; text-align: left; margin-top: 10px; font-size: 0.9rem; color: #b0b0b0;">
                <span>Sentinel Bias:</span> <span class="green">{current_bias}</span>
                <span>Accuracy:</span> <span class="green">{accuracy_val}% Sniper Filter</span>
            </div>
        </div>

        <div class="card">
            <small style="color: #666">AEON-Z LIVE DATA (XAUUSD)</small>
            <div style="height: 300px; background: #000; margin-top: 10px;">
                <div id="tradingview_gold" style="height:100%;width:100%"></div>
                <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
                <script type="text/javascript">
                new TradingView.widget({{
                    "autosize": true, "symbol": "OANDA:XAUUSD", "interval": "1",
                    "timezone": "Africa/Lagos", "theme": "dark", "style": "1",
                    "locale": "en", "container_id": "tradingview_gold"
                }});
                </script>
            </div>
        </div>

        <div class="terminal">
            <div class="green">[SYS] WhyzeD Core Connected...</div>
            <div class="green">[LOG] Sentinel Bias: {current_bias}</div>
            <div class="green">[LOG] Mode: Aggressive Demo Testing</div>
        </div>

        <div style="margin-top: 20px; font-size: 0.6rem; color: #555;">
            COURTESY: BAYELSA STATE, NIGERIA
        </div>
    </body>
    </html>
    """
    return render_template_string(html_template)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
