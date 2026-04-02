import requests
import time
import json

# Your active Cloudflare Tunnel URL
API_URL = "https://attempting-advisors-fonts-lucas.trycloudflare.com/track"

# Movement path: Starting far, moving into the geofence, then speeding
path = [
    {"lat": 6.5100, "lng": 3.3600, "speed": 15},
    {"lat": 6.5200, "lng": 3.3700, "speed": 25},
    {"lat": 6.5244, "lng": 3.3792, "speed": 40},  # Enters "Home Office"
    {"lat": 6.5250, "lng": 3.3800, "speed": 135} # Speed Anomaly!
]

def run_simulation():
    print("--- GEOPULSE SIMULATION STARTED ---")
    for i, point in enumerate(path):
        payload = {
            "userId": "sim_user_01",
            "lat": point["lat"],
            "lng": point["lng"],
            "speed": point["speed"]
        }
        try:
            response = requests.post(API_URL, json=payload)
            data = response.json()
            
            print(f"Step {i+1}: Moving to {point['lat']}, {point['lng']}")
            print(f"      | Geofences: {data.get('geofences')}")
            print(f"      | AI Anomaly: {data.get('ai').get('anomaly')}")
            print(f"      | AI Prediction: {data.get('ai').get('prediction')}")
            print("-" * 40)
            
        except Exception as e:
            print(f"Error connecting to backend: {e}")
        
        time.sleep(2) # Pause for 2 seconds between "steps"

if __name__ == "__main__":
    run_simulation()
