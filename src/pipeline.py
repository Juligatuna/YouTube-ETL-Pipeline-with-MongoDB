
import os
from pymongo import MongoClient
from dotenv import load_dotenv

from src.extract import fetch_youtube_data
from src.transform import clean_youtube_data
from src.load import insert_to_mongo

# Load environment variables
load_dotenv()

API_KEY = os.getenv("YOUTUBE_API_KEY")
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DB_NAME = os.getenv("MONGO_DB", "youtube_etl")
COLLECTION_NAME = os.getenv("MONGO_COLLECTION", "videos")

def run_pipeline():
    print("🚀 Starting ETL pipeline...")

    # 1. Extract
    print("📥 Extracting data from YouTube API...")
    raw_data = fetch_youtube_data(API_KEY, query="data engineering", max_results=10)

    # 2. Transform
    print("🧹 Transforming data...")
    df = clean_youtube_data(raw_data)

    # 3. Load
    print("💾 Loading data into MongoDB...")
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    collection = db[COLLECTION_NAME]

    inserted = insert_to_mongo(collection, df)
    print(f"✅ Inserted {inserted} records into MongoDB collection '{COLLECTION_NAME}'.")

if __name__ == "__main__":
    run_pipeline()
