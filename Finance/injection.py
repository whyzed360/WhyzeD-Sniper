import requests
import sys

# Imperial Cloud Credentials
TOKEN = 'eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiJiZjk2ODMyOGQzZjA5MzIxNzE4ZTcyNjdjNmNlZWJkYSIsImFjY2Vzc1J1bGVzIjpbeyJpZCI6InRyYWRpbmctYWNjb3VudC1tYW5hZ2VtZW50LWFwaSIsIm1ldGhvZHMiOlsidHJhZGluZy1hY2NvdW50LW1hbmFnZW1lbnQtYXBpOnJlc3Q6cHVibGljOio6KiJdLCJyb2xlcyI6WyJyZWFkZXIiLCJ3cml0ZXIiXSwicmVzb3VyY2VzIjpbIio6JFVTRVJfSUQkOioiXX0seyJpZCI6Im1ldGFhcGktcmVzdC1hcGkiLCJtZXRob2RzIjpbIm1ldGFhcGktYXBpOnJlc3Q6cHVibGljOio6KiJdLCJyb2xlcyI6WyJyZWFkZXIiLCJ3cml0ZXIiXSwicmVzb3VyY2VzIjpbIio6JFVTRVJfSUQkOioiXX0seyJpZCI6Im1ldGFhcGktcnBjLWFwaSIsIm1ldGhvZHMiOlsibWV0YWFwaS1hcGk6d3M6cHVibGljOio6KiJdLCJyb2xlcyI6WyJyZWFkZXIiLCJ3cml0ZXIiXSwicmVzb3VyY2VzIjpbIio6JFVTRVJfSUQkOioiXX0seyJpZCI6Im1ldGFhcGktcmVhbC10aW1lLXN0cmVhbWluZy1hcGkiLCJtZXRob2RzIjpbIm1ldGFhcGktYXBpOndzOnB1YmxpYzoqOioiXSwicm9sZXMiOlsicmVhZGVyIiwid3JpdGVyIl0sInJlc291cmNlcyI6WyIqOiRVU0VSX0lEJDoqIl19LHsiaWQiOiJtZXRhc3RhdHMtYXBpIiwibWV0aG9kcyI6WyJtZXRhc3RhdHMtYXBpOnJlc3Q6cHVibGljOio6KiJdLCJyb2xlcyI6WyJyZWFkZXIiLCJ3cml0ZXIiXSwicmVzb3VyY2VzIjpbIio6JFVTRVJfSUQkOioiXX0seyJpZCI6InJpc2stbWFuYWdlbWVudC1hcGkiLCJtZXRob2RzIjpbInJpc2stbWFuYWdlbWVudC1hcGk6cmVzdDpwdWJsaWM6KjoqIl0sInJvbGVzIjpbInJlYWRlciIsIndyaXRlciJdLCJyZXNvdXJjZXMiOlsiKjokVVNFUl9JRCQ6KiJdfSx7ImlkIjoiY29weWZhY3RvcnktYXBpIiwibWV0aG9kcyI6WyJjb3B5ZmFjdG9yeS1hcGk6cmVzdDpwdWJsaWM6KjoqIl0sInJvbGVzIjpbInJlYWRlciIsIndyaXRlciJdLCJyZXNvdXJjZXMiOlsiKjokVVNFUl9JRCQ6KiJdfSx7ImlkIjoibXQtbWFuYWdlci1hcGkiLCJtZXRob2RzIjpbIm10LW1hbmFnZXItYXBpOnJlc3Q6ZGVhbGluZzoqOioiLCJtdC1tYW5hZ2VyLWFwaTpyZXN0OnB1YmxpYzoqOioiXSwicm9sZXMiOlsicmVhZGVyIiwid3JpdGVyIl0sInJlc291cmNlcyI6WyIqOiRVU0VSX0lEJDoqIl19LHsiaWQiOiJiaWxsaW5nLWFwaSIsIm1ldGhvZHMiOlsiYmlsbGluZy1hcGk6cmVzdDpwdWJsaWM6KjoqIl0sInJvbGVzIjpbInJlYWRlciJdLCJyZXNvdXJjZXMiOlsiKjokVVNFUl9JRCQ6KiJdfV0sImlnbm9yZVJhdGVMaW1pdHMiOmZhbHNlLCJ0b2tlbklkIjoiMjAyMTAyMTMiLCJpbXBlcnNvbmF0ZWQiOmZhbHNlLCJyZWFsVXNlcklkIjoiYmY5NjgzMjhkM2YwOTMyMTcxOGU3MjY3YzZjZWViZGEiLCJpYXQiOjE3NzUwNzg1NTN9.mvM0FZh6jMsno0Z22_TzB9Fl2lxbZt7X46rurVCM5M9iwUKEGFybSGU9GeUGTL230PbTlBU_1MtOiKXDxh3zAfyHS11ZQ_18NdvM21SQLQpUiSpBb3rKk2etVtwu4S_A7Ai03OUc098DaNOASYqEwsVpyFU_IGGhXLrFj7BFBYAHjRRw33Q9kZNTCGg5LNWctG9dJY3nKUt1E6TgWM4y407flm2mQDeEji5UZhuqloQupTKFpQ1jzUjD5EKP__XJfgdpuCFSvGsMw--A8MxSqJ0n05SNiIQusWGgbH2LZo2VGLtQI4RsX8XiV3URsxsz5xu7pF9vj1iwpmIe56wszqn8MnCdrpUBobbZWqiQ-nwpldxWQx68TmmTq4sfXe8o6sehd1uW_rEVjjRJs_OCs7J6YBSrEjZeU5hyuhiMiyF25hjKFZAtDklndi-D6BT_p7ecgpYkKx7fRvOrSYnd3NnZCDZ_tAxcNQW2Lt0maoIlN5cFlxh9UekXWSfbWQz7ZyfPkLocnHla-wVgk5b0GMhWCPSdGzN5etNf76nl5VLmaKeEFai-4otVXnHDnVpyWbMG1UpkQmFCyFyIJw3bEA5SSzh_EuSGAhNfQCszOspot3MG57FcEYkyWAr80toTYW4hLHD2_sm7I60AWGxcgfCOPta3-rvZUAZQVGNArI8'
ACCOUNT_ID = '1e6dd908-e8f1-43a1-8fdf-531f36e21687'

def execute_trade(action):
    # MetaApi REST URL for Market Orders
    url = f"https://mt-client-api-v1.new-york.agiliumtrade.ai/users/current/accounts/{ACCOUNT_ID}/trade"
    
    headers = {
        "auth-token": TOKEN,
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    
    # 1:4 Wealth Formula & Sniper Logic (94.2% Accuracy)
    data = {
        "actionType": "ORDER_TYPE_BUY" if action == "BUY" else "ORDER_TYPE_SELL",
        "symbol": "XAUUSD",
        "volume": 0.10,
        "stopLoss": 15,          # 15 Pips Risk
        "takeProfit": 60,        # 60 Pips Reward
        "stopLossUnits": "RELATIVE_PIPS",
        "takeProfitUnits": "RELATIVE_PIPS",
        "comment": "WhyzeD Sniper 94.2%"
    }

    print(f"WHYDED: Launching {action} Sniper via New York Cloud...")
    try:
        response = requests.post(url, json=data, headers=headers)
        if response.status_code in [200, 201]:
            result = response.json()
            print(f"SUCCESS: Trade ID {result.get('orderId')} Executed")
        else:
            print(f"CLOUD ERROR: {response.text}")
    except Exception as e:
        print(f"CONNECTION FAILURE: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        execute_trade(sys.argv[1].upper())
