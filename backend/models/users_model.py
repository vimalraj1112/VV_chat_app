from flask import Flask,jsonify
from config.db import get_db_connection

def find_all_users():
    

        conn=get_db_connection()
        cursor=conn.cursor(dictionary=True)

        query = "SELECT id,username,email FROM users"

        cursor.execute(query)
        users=cursor.fetchall()

        cursor.close()
        conn.close()

        return users
    

