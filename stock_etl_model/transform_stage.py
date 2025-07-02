import pandas as pd
import logging

class Transform:
    @staticmethod
    def column_rename_fun(df):
        rename_col = {}
        for column in df.columns:
            new_name = column.split(" ")[1]
            rename_col[column] = new_name
        logging.info(f"Renamed columns: {rename_col}")
        return rename_col

    @staticmethod
    def Transform_stage(data):
        logging.info(f"Meta-Data of stock:\n {data['Meta Data']}")
        logging.info("Starting transformation stage...")


        meta_data = data['Meta Data']
        stock_name = meta_data['2. Symbol']
        last_refreshed_date = meta_data['3. Last Refreshed']
        logging.info(f"Last Refreshed Date of {stock_name} stock : {last_refreshed_date}")


        df = pd.DataFrame.from_dict(data['Time Series (Daily)'], orient='index')
        df = df.rename(columns=Transform.column_rename_fun(df))
        df.index.name = "Date"
        
        logging.info(f"Transformation has completed. Ready for Loading Phase")
        return df

# Configure logging at module level (not inside class)
logging.basicConfig(
    filename="/mnt/e/2025/Airflow/stock_etl_model/logs/etl_pipeline_transform.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
