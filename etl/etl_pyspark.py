import requests
import os

from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

URL_BASE = "https://assets-datascientest.s3.eu-west-1.amazonaws.com"
AWS_FILES = ["gps_app.csv","gps_user.csv"]

'''
    Q1. Retrieve Data from urls 
'''
def download_file(file_name:str):
    _path = f"data/{file_name}"
    if not os.path.exists(_path):
        with open(_path, 'wb') as csv_file:
            r = requests.get(url=f"{URL_BASE}/{file_name}")
            if r.status_code == 200:
                csv_file.write(r.content)
            return csv_file.read()
    with open(_path) as f:
        return f.read()

app_csv, user_csv = [ download_file(file) for file in AWS_FILES ]

'''
    Q2. Traitement de la data Rename all the column
'''
spark = SparkSession\
        .builder\
        .appName("Exam Spark")\
        .master("local[*]")\
        .getOrCreate()
        
def create_dataframe(csv_data):
    return spark.read.options(header=True, inferSchema=True, escape="\"").csv(csv_data)

def rename_columns(df):
    print(df.columns)
    for column in df.columns:
        df.withColumn(column.lower().replace(' ','_'), column)
    return df

app_df, user_df = [ rename_columns(create_dataframe(f"data/{file}")) for file in AWS_FILES ]

print(app_df.printSchema())
print(user_df.printSchema())

