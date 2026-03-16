from config.db import get_db_connection
from flask import Flask, request, jsonify
import uuid
import mysql.connector
from werkzeug.security import generate_password_hash

def create_user(username, email, password):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        user_id = str(uuid.uuid4())

        hash_password = generate_password_hash(password)

        query = "INSERT INTO users(username, email, password, id) VALUES (%s, %s, %s, %s)"
        values = (username, email, hash_password, user_id)


        cursor.execute(query, values)
        conn.commit()

        cursor.close()
        conn.close()

        return True,{
            "user":username,
            "email":email,
            "password":hash_password,
            "id":user_id
        }

    except mysql.connector.IntegrityError as e:
        # 1062 = duplicate entry
        if e.errno == 1062:
            # e.msg example: "Duplicate entry 'someone@example.com' for key 'email'"
            if "email" in e.msg:
                return False, "Email already exists!"
            elif "username" in e.msg:
                return False, "Username already exists!"
            else:
                return False, "Duplicate entry!"
        else:
            return False, f"Database error: {str(e)}"

    except Exception as e:
        return False, f"Something went wrong: {str(e)}"
    
def get_user_by_email(email):
    try:
        conn = get_db_connection()
        cursor=conn.cursor(dictionary=True)

        query= "SELECT * FROM USERS WHERE email=%s"
        value=(email,)

        cursor.execute(query,value)
        user=cursor.fetchone()

        cursor.close()
        conn.close()

        return user

    except Exception as e:
        
        return None
