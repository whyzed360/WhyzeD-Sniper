from flask import Flask, render_template_string
import os
import random

app = Flask(__name__)

@app.route('/')
def home():
    # SCALPING PARAMETERS
    accuracy_val = 50.0  # High frequency
    risk_reward = "1:1.5" # Tight ratio for quick exits
    mode = "SCALPING"
    
    # Active Scalp Bias
    current_bias = random.choice(["BULLISH (SCALP)", "BEARISH (SCALP)"])
    
    html_template = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>WHYZED SNIPER | SCALPER HUB</title>
        <style>
            :root {{
                --bg-imperial: #3b0101;
                --card-void: #0a0000;
                --neon-green: #00ff41;
                --blood-red: #ff3131;
            }}
            body {{ background-color: var(--bg-imperial); color: #fff; font-family: sans-serif; text-align: center; padding: 15px; margin: 0; }}
            .card {{ background: var(--card-void); border-radius: 20px; padding: 20px; margin-bottom: 15px; box-shadow: 0 10px 30px #000; max-width: 400px; margin: auto; border: 1px solid #5a0101; }}
            .green {{ color: var(--neon-green); font-weight: bold; }}
            .red-dot {{ width: 12px; height: 12px; background: var(--neon-green); border-radius: 50%; display: inline-block; box-shadow: 0 0 10px var(--neon-green); }}
            .terminal {{ background: #000; padding: 15px; border-radius: 15px; font-family: monospace; font-size: 0.8rem; text-align: left; border-left: 3px solid var(--neon-green); max-width: 370px; margin: 0 auto; }}
        </style>
    </head>
    <body>
        <div style="margin-top: 10px;">
            <h1 style="font-style: italic; margin: 0; letter-spacing: 2px;">WHYZED SCALPER</h1>
            <p style="font-size: 0.7rem; color: #888; margin-bottom: 20px;">MODE: HIGH FREQUENCY EXECUTION</p>
        </div>

        <div class="card">
            <div style="display: flex; justify-content: space-between;">
                <div style="text-align: left;"><small style="color: #666">SCALP STATUS</small><h2 style="font-size: 2.2rem; margin: 0;">ACTIVE</h2></div>
                <div class="red-dot"></div>
            </div>
            <div style="display: grid; grid-template-columns: 1fr 1fr; text-align: left; margin-top: 15px; font-size: 0.9rem; color: #b0b0b0;">
                <span>Sentinel Bias:</span> <span class="green">{current_bias}</span>
                <span>TP Target:</span> <span class="green">Tight (5-10 Pips)</span>
                <span>Accuracy:</span> <span class="green">{accuracy_val}%</span>
            </div>
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
            <div class="green">[SYS] Scalping Mode: ENABLED</div>
            <div class="green">[LOG] Bias: {current_bias}</div>
            <div class="green">[LOG] Entering micro-position...</div>
            <div class="green">[LOG] Quick TP target set.</div>
        </div>

        <div style="margin-top: 25px; font-size: 0.65rem; color: #777;">
            © 2026, WhyzeD Empire | Bayelsa State, Nigeria
        </div>
    </body>
    </html>
    """
    return render_template_string(html_template)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
