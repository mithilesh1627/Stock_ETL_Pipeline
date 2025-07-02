from airflow.decorators import dag,task
from datetime import datetime,timedelta
import sys
import os
import json
import streamlit as st
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'stock_etl_model')))
from extract_stage import Extract
from transform_stage import Transform
from load_stage import Load

default_args = {
    "owner":"Mithilesh",
    "start_date" : datetime(2025,7,2),
    "retries":1,
    'retry_delay': timedelta(minutes=1),
    "end_date": datetime(2025,7,5)
}

@dag( dag_id="Stock_etl_pipeline",
    default_args=default_args,
    schedule_interval="@daily",
    catchup=False,
    tags=["stock", "ETL", "IBM"],
    max_active_tasks=1)
def stock_etl_dag():
    @task()
    def get_config():
        with open("/mnt/e/2025/Airflow/stock_etl_model/password.json", 'r') as file:
            return json.load(file)
        
    @task()
    def extract_config_values(config: dict):
        return {
            "symbol": config["symbol"],
            "password": config["password"],
            "mongo_uri": config["mongo_uri"],
            "db_name": config["db_name"],
            "collection_name": config["collection_name"]
        }
    
    @task()
    def extract(config: dict):
        extractor = Extract()
        return extractor.Extract_stage(config["symbol"], config["password"])
    
    @task()
    def transform(data: dict):
        return Transform.Transform_stage(data)

    @task()
    def load(data, config: dict):
        return Load.Load_stage(data,
                               config["mongo_uri"],
                               config["db_name"],
                               config["collection_name"]
                               )


    config = get_config()
    config_values = extract_config_values(config)




    raw_data = extract(config_values)
    transformed_data = transform(raw_data)
    message = load(data=transformed_data,config=config_values)
    print(message)
    
etl_dag = stock_etl_dag()

