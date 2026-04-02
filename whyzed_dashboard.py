from flask import Flask, render_template_string
import os

app = Flask(__name__)

@app.route('/')
def home():
    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body { background-color: #3b0101; color: #fff; font-family: monospace; text-align: center; padding: 20px; }
            .card { background: #000; border: 1px solid #ff3131; border-radius: 15px; padding: 20px; max-width: 400px; margin: auto; }
            .green { color: #00ff41; }
            .terminal { background: #000; padding: 15px; border-left: 3px solid #00ff41; text-align: left; font-size: 0.8rem; margin-top: 20px; }
        </style>
    </head>
    <body>
        <h1>WHYZED SCALPER V2</h1>
        <div class="card">
            <h2 class="green">SIGNAL BRIDGE: ACTIVE</h2>
            <p>Strategy: Scrapping (Micro Profit)</p>
            <p>Wealth Formula: 1:2 Ratio</p>
        </div>
        <div class="terminal">
            <div class="green">[LOG] Mode: High Frequency Scalp</div>
            <div class="green">[LOG] Target: XAUUSD (Gold)</div>
            <div class="green">[LOG] © 2026, WhyzeD Empire.</div>
        </div>
    </body>
    </html>
    """
    return render_template_string(html_template)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
