from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

# Define default arguments
default_args = {
    'owner': 'admin',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
dag = DAG(
    'hello_world',
    default_args=default_args,
    description='A simple hello world DAG',
    schedule_interval=timedelta(days=1),
    catchup=False,
    tags=['example'],
)

def print_hello():
    """Simple function to print hello world"""
    print("Hello World from Airflow!")
    return "Hello World from Airflow!"

def print_date():
    """Function to print current date"""
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {current_date}")
    return current_date

# Define tasks
hello_task = PythonOperator(
    task_id='print_hello',
    python_callable=print_hello,
    dag=dag,
)

date_task = PythonOperator(
    task_id='print_date',
    python_callable=print_date,
    dag=dag,
)

# Set task dependencies
hello_task >> date_task
