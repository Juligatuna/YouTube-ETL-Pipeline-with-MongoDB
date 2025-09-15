
def insert_to_mongo(collection, df):
    """Insert transformed DataFrame into MongoDB"""
    records = df.to_dict(orient="records")
    if records:
        result = collection.insert_many(records)
        return len(result.inserted_ids)
    return 0
