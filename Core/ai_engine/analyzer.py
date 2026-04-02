import json
from collections import Counter

ALERTS_FILE = '../backend/alerts_history.json'

def learn_behavior():
    try:
        with open(ALERTS_FILE, 'r') as f:
            data = json.load(f)
        
        if not data:
            print("No data to learn from yet.")
            return

        # 1. Frequency of Zones
        zones = [a['message'] for a in data if a['type'] == 'GEOFENCE']
        zone_counts = Counter(zones)

        # 2. Peak Anomaly Hours
        hours = [a['time'][11:13] for a in data if a['type'] == 'ANOMALY']
        hour_counts = Counter(hours)

        print("--- GEOPULSE BEHAVIOR REPORT ---")
        print(f"Total Events Logged: {len(data)}")
        
        if zone_counts:
            most_common_zone = zone_counts.most_common(1)[0]
            print(f"Primary Location: {most_common_zone[0]} (Visited {most_common_zone[1]} times)")
        
        if hour_counts:
            peak_hour = hour_counts.most_common(1)[0]
            print(f"Peak Anomaly Hour: {peak_hour[0]}:00")
            
        print("-" * 32)

    except Exception as e:
        print(f"Analysis failed: {e}")

if __name__ == "__main__":
    learn_behavior()
