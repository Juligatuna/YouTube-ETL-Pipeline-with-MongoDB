import pandas as pd

def clean_youtube_data(raw_data):
    df = pd.DataFrame(raw_data)
    df['publishedAt']=pd.to_datetime(df['publishedAt'], errors = 'coerce')
    df = df.rename(columns = {
        'videoId': 'video_id',
        'title':'video_title',
        'channel':'channel_name',
        'publishedAt':'published_at'
    })
    
    return df