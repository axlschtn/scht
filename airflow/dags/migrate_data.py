from airflow.decorators import dag, task
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago

@dag(
    dag_id="migrate_db",
    description="Collect, transform data from weather api",
    tags=["Migrate","Database","ETL"],
    schedule_interval='* * * * *',
    start_date=days_ago(0)
)
def migrate_db():
    
    @task(task_id="hello")
    def simple_hello_task():
        return PythonOperator(
            task_id="python_task",
            python_callable=lambda: print('Hi from python operator'),
        )
    
    hello = simple_hello_task() 
    hello

migrate_db()