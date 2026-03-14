from config.db import get_db_connection
from flask import Flask,request,jsonify
import uuid


def create_user(name,email,password):
    conn=get_db_connection()
    cursor=conn.cursor()
    id = str(uuid.uuid4())

    query= "INSERT INTO users(username,email,password,id) VALUES(%s,%s,%s,%s)"
    values=(name,email,password,id)

    cursor.execute(query,values)
    conn.commit()

    cursor.close()
    conn.close()
    

    return True




    
