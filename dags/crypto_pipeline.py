from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="crypto_etl_pipeline",
    start_date=datetime(2025,1,1),
    schedule="*/5 * * * *",
    catchup=False
) as dag:

    run_etl = BashOperator(
        task_id="run_crypto_etl",
        bash_command="python /opt/airflow/scripts/crypto_etl.py"    
        )
