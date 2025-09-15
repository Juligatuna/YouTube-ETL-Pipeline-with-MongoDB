from config import API_KEY
from googleapiclient.discovery import build

print("DEBUG - API_KEY from config.py:", API_KEY)

# Simple YouTube API test
def test_youtube_api():
    youtube = build("youtube", "v3", developerKey=API_KEY)
    request = youtube.search().list(
        q="data engineering",
        part="snippet",
        maxResults=2
    )
    response = request.execute()
    print("✅ API call succeeded!")
    for item in response["items"]:
        print(item["snippet"]["title"])

if __name__ == "__main__":
    test_youtube_api()
