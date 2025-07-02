import logging
import pandas as pd
import pymongo
class Load:
    @staticmethod
    def Load_stage(data,mongo_uri, db_name, collection_name):
        try:
            data = data.copy()
            data.reset_index(inplace=True)
            data['Date'] = pd.to_datetime(data['Date'])  

            records = data.to_dict(orient="records")

            client = pymongo.MongoClient(mongo_uri)
            db = client[db_name]
            collection = db[collection_name]

            collection.delete_many({})
            collection.insert_many(records)

            logging.info(f"{len(records)} records loaded into {db_name}.{collection_name}")
            return f"Load successful: {len(records)} records inserted."
        
        except Exception as e:
            logging.exception("Load stage failed.")
            return f"Load failed: {e}"

# Configure logging at module level
logging.basicConfig(
    filename="/mnt/e/2025/Airflow/stock_etl_model/logs/etl_pipeline_load.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)