import mysql.connector

def get_db_connection():
    connection=mysql.connector.connect(
        host="localhost",
        user="root",
        password="1112",
        database="vvchat_app"
    )
    return connection 



