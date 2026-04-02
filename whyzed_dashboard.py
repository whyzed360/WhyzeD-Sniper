from flask import Flask, render_template_string
import os
import random

app = Flask(__name__)

@app.route('/')
def home():
    # 50% Accuracy - High Frequency Test Mode
    accuracy_val = 50.0
    
    # 1:2 Ratio Logic
    risk = 1
    reward = 2
    
    # Forced Active Bias (No more Neutral)
    current_bias = random.choice(["BULLISH", "BEARISH"])
    
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
            .card {{ background: var(--card-void); border-radius: 20px; padding: 20px; margin-bottom: 15px; box-shadow: 0 10px 30px #000; max-width: 400px; margin: auto; border: 1px solid #440000; }}
            .green {{ color: var(--neon-green); font-weight: bold; }}
            .red-dot {{ width: 12px; height: 12px; background: var(--blood-red); border-radius: 50%; display: inline-block; box-shadow: 0 0 10px var(--blood-red); }}
            .terminal {{ background: #000; padding: 15px; border-radius: 15px; font-family: monospace; font-size: 0.8rem; text-align: left; border-left: 3px solid var(--blood-red); max-width: 370px; margin: 0 auto; }}
            .progress-bar {{ height: 10px; background: #111; border-radius: 5px; margin: 10px 0; overflow: hidden; border: 1px solid #300; }}
            .fill {{ width: 50%; height: 100%; background: linear-gradient(90deg, #600, var(--blood-red)); }}
        </style>
    </head>
    <body>
        <div style="margin-top: 10px;">
            <h1 style="font-style: italic; margin: 0; letter-spacing: 2px;">WHYZED SNIPER</h1>
            <p style="font-size: 0.7rem; color: #888; margin-bottom: 20px;">TEST MODE: AGGRESSIVE EXECUTION</p>
        </div>

        <div class="card">
            <div style="display: flex; justify-content: space-between; align-items: flex-start;">
                <div style="text-align: left;">
                    <small style="color: #666">BOT STATUS</small>
                    <h2 style="font-size: 2.2rem; margin: 0;">ACTIVE</h2>
                </div>
                <div class="red-dot"></div>
            </div>
            <div style="display: grid; grid-template-columns: 1fr 1fr; text-align: left; margin-top: 15px; font-size: 0.9rem; color: #b0b0b0;">
                <span>Sentinel Bias:</span> <span class="green">{current_bias}</span>
                <span>Accuracy:</span> <span class="green">{accuracy_val}% (Aggressive)</span>
            </div>
        </div>

        <div class="card">
            <div style="display:flex; justify-content:space-between; font-size: 0.7rem;">
                <span>RISK: {risk}</span> <span>REWARD: {reward}</span>
            </div>
            <div class="progress-bar"><div class="fill"></div></div>
            <p style="color: #666; font-size: 0.7rem;">WhyzeD 1:2 WEALTH FORMULA (TEST)</p>
        </div>

        <div class="card">
            <div id="tradingview_gold" style="height:300px;width:100%"></div>
            <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
            <script type="text/javascript">
            new TradingView.widget({{
                "autosize": true, "symbol": "OANDA:XAUUSD", "interval": "1",
                "timezone": "Africa/Lagos", "theme": "dark", "style": "1",
                "locale": "en", "container_id": "tradingview_gold"
            }});
            </script>
        </div>

        <div class="terminal">
            <div style="color: var(--blood-red)">[SYS] Institutional Filter: DISABLED</div>
            <div class="green">[LOG] Sentinel Bias: {current_bias}</div>
            <div class="green">[LOG] Target Found. Executing trade...</div>
        </div>

        <div style="margin-top: 25px; font-size: 0.65rem; color: #ffd700; letter-spacing: 1px;">
            COURTESY: BAYELSA STATE, NIGERIA
        </div>
    </body>
    </html>
    """
    return render_template_string(html_template)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
