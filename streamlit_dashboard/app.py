import streamlit as st
import pandas as pd
import pymongo
import json
class Visualize:
    @staticmethod
    def load_data(MONGO_URI, DB_NAME, COLLECTION_NAME):
        client = pymongo.MongoClient(MONGO_URI)
        db = client[DB_NAME]
        collection = db[COLLECTION_NAME]
        data = list(collection.find({}, {"_id": 0}))
        df = pd.DataFrame(data)
        if 'Date' in df.columns:
            df['Date'] = pd.to_datetime(df['Date'])
            df.sort_values("Date", inplace=True)
        return df


    @staticmethod
    def visual(MONGO_URI, DB_NAME, COLLECTION_NAME):
        st.title(" IBM Stock Data Dashboard")
        df = Visualize.load_data(MONGO_URI, DB_NAME, COLLECTION_NAME)
        if df.empty:
            st.warning("No data found in MongoDB.")
        else:
            st.subheader(" Latest Records")
            st.dataframe(df.tail(10), use_container_width=True)

            st.subheader(" Stock Price Trend")
            st.line_chart(df.set_index("Date")["close"])

with open("/mnt/e/2025/Airflow/stock_etl_model/password.json", 'r') as file:
     config = json.load(file)
    
Visualize.visual(MONGO_URI=config["mongo_uri"], DB_NAME=config["db_name"], COLLECTION_NAME=config["collection_name"])