import os
import yaml
from dotenv import load_dotenv
from pymongo import MongoClient
from utils.youtube_api import fetch_youtube_data
from utils.transform import clean_youtube_data

# Load secrets from .env
load_dotenv()
API_KEY = os.getenv("YOUTUBE_API_KEY")
MONGO_URI = os.getenv("MONGO_URI")

# Load safe config
with open("config/config.yaml", "r") as f:
    config = yaml.safe_load(f)

# 1. Extract
raw_data = fetch_youtube_data(API_KEY, 
                              query=config["query"]["search_term"], 
                              max_results=config["query"]["max_results"])

# 2. Transform
df = clean_youtube_data(raw_data)

# 3. Load
client = MongoClient(MONGO_URI)
db = client[config["database"]["db"]]
collection = db[config["database"]["collection"]]

records = df.to_dict(orient="records")
if records:
    collection.insert_many(records)
    print(f"Inserted {len(records)} records into MongoDB")
else:
    print("No data to insert")
