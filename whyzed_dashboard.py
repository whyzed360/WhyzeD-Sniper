from flask import Flask, render_template_string
import os

app = Flask(__name__)

# THE EXACT "IMPERIAL EXECUTION HUB" LAYOUT
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>WHYZED SNIPER | IMPERIAL EXECUTION HUB</title>
    <style>
        :root {
            --bg-imperial: #3b0101;
            --card-void: #0a0000;
            --neon-green: #00ff41;
            --blood-red: #ff3131;
        }

        body {
            background-color: var(--bg-imperial);
            color: #ffffff;
            font-family: 'Segoe UI', sans-serif;
            margin: 0;
            padding: 15px;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        .main-header {
            text-align: center;
            margin-bottom: 20px;
        }

        .main-header h1 {
            font-style: italic;
            font-weight: 900;
            letter-spacing: 2px;
            margin: 0;
            font-size: 1.8rem;
        }

        .main-header p {
            font-size: 0.7rem;
            color: #888;
            letter-spacing: 1px;
        }

        .container {
            width: 100%;
            max-width: 400px;
            display: flex;
            flex-direction: column;
            gap: 15px;
        }

        .card {
            background-color: var(--card-void);
            border-radius: 20px;
            padding: 20px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        }

        .status-header {
            display: flex;
            justify-content: space-between;
        }

        .status-header h2 { font-size: 2.2rem; margin: 0; }

        .red-dot {
            width: 12px;
            height: 12px;
            background: var(--blood-red);
            border-radius: 50%;
            box-shadow: 0 0 15px var(--blood-red);
        }

        .stats-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 5px;
            font-size: 0.9rem;
            margin-top: 10px;
            color: #b0b0b0;
        }

        .green { color: var(--neon-green); }

        .chart-area {
            height: 320px;
            background: #000;
            border-radius: 10px;
            margin-top: 10px;
            border: 1px solid #222;
        }

        .wealth-formula {
            text-align: center;
            font-size: 0.7rem;
        }

        .progress-bar {
            height: 10px;
            background: #111;
            border-radius: 5px;
            margin: 10px 0;
            overflow: hidden;
            border: 1px solid #300;
        }

        .fill {
            width: 85%;
            height: 100%;
            background: linear-gradient(90deg, #600, var(--blood-red));
        }

        .terminal {
            background: #000;
            border-radius: 15px;
            padding: 15px;
            font-family: 'Courier New', monospace;
            font-size: 0.8rem;
            border: 1px solid #111;
        }

        .footer-courtesy {
            margin-top: 20px;
            font-size: 0.6rem;
            color: #555;
            text-align: center;
            letter-spacing: 1px;
        }
    </style>
</head>
<body>
    <div class="main-header">
        <h1>WHYZED SNIPER</h1>
        <p>IMPERIAL EXECUTION HUB</p>
    </div>

    <div class="container">
        <div class="card">
            <div class="status-header">
                <div>
                    <small style="color: #666">BOT STATUS</small>
                    <h2>ACTIVE</h2>
                </div>
                <div class="red-dot"></div>
            </div>
            <div class="stats-grid">
                <span>Sentinel Bias:</span> <span>NEUTRAL</span>
                <span>Accuracy:</span> <span class="green">75.0% Sniper Filter</span>
                <span>Last Sync:</span> <span>23:56:16</span>
            </div>
        </div>

        <div class="card">
            <small style="color: #666">AEON-Z SYNCED LIVE DATA (XAUUSD)</small>
            <div class="chart-area">
                <div id="tradingview_gold" style="height:100%;width:100%"></div>
                <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
                <script type="text/javascript">
                new TradingView.widget({
                    "autosize": true,
                    "symbol": "OANDA:XAUUSD",
                    "interval": "1",
                    "timezone": "Africa/Lagos",
                    "theme": "dark",
                    "style": "1",
                    "locale": "en",
                    "container_id": "tradingview_gold"
                });
                </script>
            </div>
        </div>

        <div class="wealth-formula">
            <div style="display:flex; justify-content:space-between">
                <span>RISK: 1</span> <span>REWARD: 4</span>
            </div>
            <div class="progress-bar"><div class="fill"></div></div>
            <p style="color: #666">WhyzeD 1:4 WEALTH FORMULA</p>
        </div>

        <div class="terminal">
            <div class="green">[SYS] WhyzeD Core Connected...</div>
            <div class="green">[LOG] Sentinel Bias: NEUTRAL</div>
            <div class="green">[LOG] Filter Ready: False</div>
        </div>

        <div class="footer-courtesy">
            © 2026 Bayelsa State.
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
