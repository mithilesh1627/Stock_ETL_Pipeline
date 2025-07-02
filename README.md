# 📈 Stock Market ETL Pipeline with Apache Airflow & Streamlit

This project automates the daily extraction, transformation, and loading (ETL) of stock market data using **Apache Airflow**, with data stored in **MongoDB** and visualized using a **Streamlit dashboard**.

> ✅ Designed to reflect a real-world, modular Data Engineering pipeline.
> 🏢 Built with production-style practices.
---

## 🚀 Tech Stack

- **Apache Airflow** – DAG orchestration  
- **Python** – ETL logic  
- **MongoDB** – NoSQL data storage  
- **Streamlit** – Dashboard for data visualization  
- **JSON** – Config-based design for modularity

---

## 📌 Features

- Modular architecture: `Extract`, `Transform`, and `Load` stages are separated as Python modules
- Scheduled DAG runs with retry logic and email alerts
- Secure config loading via JSON (excluded from repo)
- XCom-based task communication between tasks
- Integrated Streamlit dashboard for visualizing processed stock data

---

## 🗂️ Project Structure

```
stock-etl-pipeline/
├── dags/
│   └── etl_stock_pipeline.py         # Main Airflow DAG
├── stock_etl_model/
│   ├── extract_stage.py              # Data extraction logic
│   ├── transform_stage.py            # Transformation rules
│   └── load_stage.py                 # MongoDB loading logic
├── streamlit_dashboard/
│   └── dashboard.py                  # Streamlit app for visualization
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🧪 How It Works

1. **`get_config` Task**  
   Reads credentials and config values from a local `password.json` (excluded from repo).
2. **`extract` Task**  
   Fetches stock data via APIs using credentials.
3. **`transform` Task**  
   Cleans and structures raw data for analysis.
4. **`load` Task**  
   Inserts final dataset into MongoDB.
5. **Dashboard**  
   A separate Streamlit app reads from MongoDB and displays charts like volume and close price trends.

---

## 📊 Streamlit Dashboard Preview

> 

---

## 🛠️ Setup Instructions

```bash
# Clone the repository
git clone https://github.com/your-username/stock-etl-pipeline.git

# Navigate to project
cd stock-etl-pipeline

# Create and activate a virtual environment
python -m venv airflow_venv
source airflow_venv/bin/activate  # Linux/Mac
airflow_venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Start Airflow
export AIRFLOW_HOME=~/airflow
airflow db init
airflow webserver --port 8080
airflow scheduler

# Start Streamlit 
streamlit run streamlit_dashboard/dashboard.py
```

---

## 🔒 Environment Configuration

> ⚠️ Sensitive values like API keys, Mongo URI, and credentials are stored in `password.json` which is excluded via `.gitignore`.

---

## 🧠 What I Learned

- Designing modular, production-ready ETL pipelines
- Implementing XCom-based communication in Airflow
- Managing DAG scheduling, retries, and failure handling
- Visualizing real-time data with Streamlit
- Clean code organization for collaborative projects

---

## 🙋‍♂️ About Me

I'm a Data Engineer passionate about building practical, real-world pipelines. Currently strengthening my ML & engineering skills with hands-on projects.  
**Let’s connect:** [LinkedIn → Mithilesh Chaurasiya](https://www.linkedin.com/in/mithilesh1627)
