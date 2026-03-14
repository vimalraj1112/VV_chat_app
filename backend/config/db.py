import mysql.connector
import os

db_host=os.getenv("DB_HOST")
db_user=os.getenv("DB_USER")
db_password=os.getenv("DB_PASSWORD")
db_database=os.getenv("DB_DATABASE")

def get_db_connection():
    connection=mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_database
    )
    return connection 


