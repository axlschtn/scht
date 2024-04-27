from airflow.decorators import dag, task
from airflow.utils.dates import days_ago
from airflow.providers.postgres.hooks.postgres import PostgresHook

'''
    Providers list : https://github.com/apache/airflow/blob/main/airflow/providers/
    for mysql providers => 
        - providers Mysql 
    Exemple: 
        from airflow.providers.postgres.hooks.postgres import PostgresHook
'''

@dag(
    dag_id="maria_db_to_bq",
    description="Collect, transform data from weather api",
    tags=["Migrate","Database","ETL"],
    schedule_interval='* * * * *',
    start_date=days_ago(0)
)
def maria_db_to_bq():   
    test = "ok"
    print(test)
    
maria_db_to_bq()