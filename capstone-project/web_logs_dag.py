from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'Ahmed Saied',
    'depends_on_past': False,
    'start_date': datetime(2023, 6, 14),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

dag = DAG(
    'process_web_log',
    description='Extract data from a web server log file, Transform the data, Load the transformed data into a tar file',
    default_args=default_args,
    schedule_interval='@daily',
)

extract = BashOperator(
    task_id='extract_ips_from_logs',
    #split columns with delimter ' ', retrive field number 1
    bash_command="cd /home/project/airflow/dags/capstone; cut -d' ' -f1 accesslog.txt > extracted_data.txt;",
    dag=dag,
)

transform = BashOperator(
    task_id='filter_ips',
    bash_command="cd /home/project/airflow/dags/capstone; grep -v '198.46.149.143' extracted_data.txt > transformed_data.txt",
    dag=dag,
)

load = BashOperator(
    task_id='archive_ips',
    bash_command="cd /home/project/airflow/dags/capstone; tar -cvf weblog.tar transformed_data.txt",
    dag=dag,
)

extract >> transform >> load