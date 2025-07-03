import streamlit as st
import pandas as pd
import pymongo
import json
import altair as alt
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
        st.title("IBM Stock Data Dashboard")
        df = Visualize.load_data(MONGO_URI, DB_NAME, COLLECTION_NAME)

        if df.empty:
            st.warning("No data found in MongoDB.")
        else:
            st.subheader("Latest Records")
            st.dataframe(df.tail(10), use_container_width=True)

            st.subheader("Interactive Stock Price Trend")

            if "Date" in df.columns and "close" in df.columns:
                chart = alt.Chart(df).mark_line().encode(
                    x=alt.X("Date:T", title="Date"),
                    y=alt.Y("close:Q", title="Closing Price"),
                    tooltip=["Date", "close"]
                ).interactive()  
                st.altair_chart(chart, use_container_width=True)
            else:
                st.error("Required columns 'Date' and 'close' not found in data.")

with open("/mnt/e/2025/Airflow/stock_etl_model/password.json", 'r') as file:
    config = json.load(file)

Visualize.visual(
    MONGO_URI=config["mongo_uri"],
    DB_NAME=config["db_name"],
    COLLECTION_NAME=config["collection_name"]
)
