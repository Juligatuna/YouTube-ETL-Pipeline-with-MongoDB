YouTube ETL Pipeline (MongoDB)

This project extracts video data from the YouTube Data API, transforms it into a clean format, and loads it into a MongoDB database for further analysis (via Jupyter Notebooks).

```bash
📂 Project Structure
aws-etl-youtube-pipeline/
│── README.md
│── requirements.txt
│
├── config/
│   └── config.yaml        
│
├── src/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   ├── utils.py
│   └── pipeline.py         # Or etl_to_mongo.py (main script)
│
├── data/
│   └── youtube_videos.csv/          # YouTube video data
│
├── notebooks/
│   └── Youtube Analysis from MongoDB.ipynb     # Jupyter notebook for EDA & visualization
│
└── tests/
    └── test_pipeline.py

```

🚀 Setup Instructions
1. Clone the Repository
git clone https://github.com/<your-username>/aws-etl-youtube-pipeline.git
cd aws-etl-youtube-pipeline

2. Create & Activate Virtual Environment
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

3. Install Dependencies
pip install -r requirements.txt

4. Configure Secrets

Create a .env file in the project root (⚠️ not committed to GitHub):

YOUTUBE_API_KEY=your_api_key_here
MONGO_URI=mongodb://localhost:27017

5. Configure Settings

Edit config/config.yaml to set query parameters and MongoDB database/collection:

database:
  db: youtube_etl
  collection: videos

query:
  search_term: "data engineering"
  max_results: 10

6. Run the ETL Pipeline
python src/pipeline.py


(or etl_to_mongo.py depending on your main script)

7. Explore Data in MongoDB

Once loaded, connect to MongoDB and query the youtube_etl.videos collection:

mongosh
use youtube_etl
db.videos.find().pretty()

📊 Analysis with Jupyter

To analyze or visualize the data:

jupyter notebook notebooks/analysis.ipynb