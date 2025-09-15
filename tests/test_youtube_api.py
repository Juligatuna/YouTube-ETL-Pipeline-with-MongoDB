import requests
import yaml

# Load config
with open("config/config.yaml", "r") as f:
    config = yaml.safe_load(f)

API_KEY = config["youtube"]["api_key"]

# Example request: search for "data engineering" videos
url = "https://www.googleapis.com/youtube/v3/search"
params = {
    "part": "snippet",
    "q": "data engineering",
    "type": "video",
    "maxResults": 3,
    "key": API_KEY
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    print("✅ API call successful!")
    for item in data["items"]:
        print(f"- {item['snippet']['title']} (Channel: {item['snippet']['channelTitle']})")
else:
    print("❌ API call failed:", response.text)
