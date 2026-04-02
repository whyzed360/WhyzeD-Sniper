import requests
import time
import numpy as np
import feedparser

# --- CONFIG ---
TOKEN = 'eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiJiZjk2ODMyOGQzZjA5MzIxNzE4ZTcyNjdjNmNlZWJkYSIsImFjY2Vzc1J1bGVzIjpbeyJpZCI6InRyYWRpbmctYWNjb3VudC1tYW5hZ2VtZW50LWFwaSIsIm1ldGhvZHMiOlsidHJhZGluZy1hY2NvdW50LW1hbmFnZW1lbnQtYXBpOnJlc3Q6cHVibGljOio6KiJdLCJyb2xlcyI6WyJyZWFkZXIiLCJ3cml0ZXIiXSwicmVzb3VyY2VzIjpbIio6JFVTRVJfSUQkOioiXX0seyJpZCI6Im1ldGFhcGktcmVzdC1hcGkiLCJtZXRob2RzIjpbIm1ldGFhcGktYXBpOnJlc3Q6cHVibGljOio6KiJdLCJyb2xlcyI6WyJyZWFkZXIiLCJ3cml0ZXIiXSwicmVzb3VyY2VzIjpbIio6JFVTRVJfSUQkOioiXX0seyJpZCI6Im1ldGFhcGktcnBjLWFwaSIsIm1ldGhvZHMiOlsibWV0YWFwaS1hcGk6d3M6cHVibGljOio6KiJdLCJyb2xlcyI6WyJyZWFkZXIiLCJ3cml0ZXIiXSwicmVzb3VyY2VzIjpbIio6JFVTRVJfSUQkOioiXX0seyJpZCI6Im1ldGFhcGktcmVhbC10aW1lLXN0cmVhbWluZy1hcGkiLCJtZXRob2RzIjpbIm1ldGFhcGktYXBpOndzOnB1YmxpYzoqOioiXSwicm9sZXMiOlsicmVhZGVyIiwid3JpdGVyIl0sInJlc291cmNlcyI6WyIqOiRVU0VSX0lEJDoqIl19LHsiaWQiOiJtZXRhc3RhdHMtYXBpIiwibWV0aG9kcyI6WyJtZXRhc3RhdHMtYXBpOnJlc3Q6cHVibGljOio6KiJdLCJyb2xlcyI6WyJyZWFkZXIiLCJ3cml0ZXIiXSwicmVzb3VyY2VzIjpbIio6JFVTRVJfSUQkOioiXX0seyJpZCI6InJpc2stbWFuYWdlbWVudC1hcGkiLCJtZXRob2RzIjpbInJpc2stbWFuYWdlbWVudC1hcGk6cmVzdDpwdWJsaWM6KjoqIl0sInJvbGVzIjpbInJlYWRlciIsIndyaXRlciJdLCJyZXNvdXJjZXMiOlsiKjokVVNFUl9JRCQ6KiJdfSx7ImlkIjoiY29weWZhY3RvcnktYXBpIiwibWV0aG9kcyI6WyJjb3B5ZmFjdG9yeS1hcGk6cmVzdDpwdWJsaWM6KjoqIl0sInJvbGVzIjpbInJlYWRlciIsIndyaXRlciJdLCJyZXNvdXJjZXMiOlsiKjokVVNFUl9JRCQ6KiJdfSx7ImlkIjoibXQtbWFuYWdlci1hcGkiLCJtZXRob2RzIjpbIm10LW1hbmFnZXItYXBpOnJlc3Q6ZGVhbGluZzoqOioiLCJtdC1tYW5hZ2VyLWFwaTpyZXN0OnB1YmxpYzoqOioiXSwicm9sZXMiOlsicmVhZGVyIiwid3JpdGVyIl0sInJlc291cmNlcyI6WyIqOiRVU0VSX0lEJDoqIl19LHsiaWQiOiJiaWxsaW5nLWFwaSIsIm1ldGhvZHMiOlsiYmlsbGluZy1hcGk6cmVzdDpwdWJsaWM6KjoqIl0sInJvbGVzIjpbInJlYWRlciJdLCJyZXNvdXJjZXMiOlsiKjokVVNFUl9JRCQ6KiJdfV0sImlnbm9yZVJhdGVMaW1pdHMiOmZhbHNlLCJ0b2tlbklkIjoiMjAyMTAyMTMiLCJpbXBlcnNvbmF0ZWQiOmZhbHNlLCJyZWFsVXNlcklkIjoiYmY5NjgzMjhkM2YwOTMyMTcxOGU3MjY3YzZjZWViZGEiLCJpYXQiOjE3NzUwODIxNDN9.kWlPahx0FZ3HznMgmxgajXil5HzBsNhwebAwNLTF3qV1X6ujeVOSMcACM3Szu15A1GIYeGUcPcoBBo3AjaukF8M7SlwCqvRDwasNa8QUsClT7sts1xSMb77ixHEBo0swAtdG_wVrFTjWAqrM5kVIL2sNS34eIug3JKpBjfBzTHqy7K9XujJFzY892kx7GxcfCnrPmrT3Mg-NAH2GT3e5se3OTZuovY8d7MYrSjUP_or9T6qNrkHzYby9F9CvSPO9W0-Utkuc4errdar7vHtvSEuk4l2Ib3LqcwDDBDBsVAULvcVTBTn7KX94SyTNQj-lKgv5HIAWG3iPxLKeKbO3uMd1aCKbVOFKwC70qLK78KCijF-9hmZY1bzSfTGWfylhMKw-qxGfaPvNJByhIFnDq6zugzT3SqizYAWRlSdUEQhazZvrSbehwcZ2_2i90oo_aeNC0_zI7QTnbaqh_H3MtkGSDV_GCi3RZthGA8UnAclEwFTl7bOfeN2bzmcGqgpNF-SFvmKxKP8ofJJ-SqY5-4HgoNNiM1qg3l3eQwibknvXd0IMBiDYYJlDo15tI95g-688MBlc4sMuLQe78rGHkGOo6mCQ2hdFwgUh5aLldSG3Wfz1ix4rMX51gVE3xuknSH6_qIp51TXLwCT8nytmhi43HLfvTx3ja4izby_27vk'
ACCOUNT_ID = 'A3397bab-9316-41f4-a3e2-fc81b336333a'

def update_dashboard(bias, ready):
    """Writes status to a bridge file for Flask to read"""
    try:
        with open('/data/data/com.termux/files/home/WHYZED_EMPIRE/Core/status.txt', 'w') as f:
            f.write(f"{bias}|{ready}|{time.strftime('%H:%M:%S')}")
    except: pass

def get_news_bias():
    feeds = ['https://www.reutersagency.com/feed/?best-topics=business-finance', 
             'http://feeds.marketwatch.com/marketwatch/topstories/']
    score = 0
    try:
        for url in feeds:
            f = feedparser.parse(url)
            for e in f.entries[:5]:
                t = e.title.lower()
                if any(w in t for w in ['growth', 'strong', 'hike']): score += 1
                if any(w in t for w in ['recession', 'weak', 'cut']): score -= 1
        if score > 1: return "SELL"
        if score < -1: return "BUY"
    except: pass
    return "NEUTRAL"

def check_filters():
    url = f"https://mt-client-api-v1.new-york.agiliumtrade.ai/users/current/accounts/{ACCOUNT_ID}/symbols/XAUUSD/fixed-period-candles/1m?limit=20"
    try:
        res = requests.get(url, headers={"auth-token": TOKEN}).json()
        highs = np.array([c['high'] for c in res])
        lows = np.array([c['low'] for c in res])
        return np.mean(highs - lows) > 0.15
    except: return False

if __name__ == "__main__":
    print("🏛️ WhyzeD Sniper: AUTO-PILOT ONLINE")
    while True:
        bias = get_news_bias()
        ready = check_filters()
        update_dashboard(bias, ready)
        # Logic to trade...
        time.sleep(60) # Sync every minute
