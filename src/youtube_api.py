

def fetch_youtube_data(api_key, query="data engineering", max_results=10):
    from googleapiclient.discovery import build
    youtube = build('youtube', 'v3',developerKey=api_key)
    request = youtube.search().list(
        q = query,
        part = 'snippet',
        maxResults = max_results
    )
    response = request.execute()

    videos = []
    for item in response.get('items',[]):
         if item["id"]["kind"] == "youtube#video":
            videos.append({
                "videoId": item["id"]["videoId"],
                "title": item["snippet"]["title"],
                "channelTitle": item["snippet"]["channelTitle"],
                "publishedAt": item["snippet"]["publishedAt"]

        })
    return videos
