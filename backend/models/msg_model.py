from flask import Flask
from config.db import get_db_connection
import uuid
from models.auth_model import get_user_by_id

def create_chat(conn):
    
    cursor=conn.cursor(dictionary=True)
    id=str(uuid.uuid4())

    query="INSERT INTO CHATS(ID,CREATED_AT) VALUES(%s,NOW())"
    values=(id,)

    cursor.execute(query,values)

    cursor.close()

    return id

def add_participants(conn,chat_id:str,participants_ids:list[str]):

    query="INSERT INTO PARTICIPANTS(ID,CHAT_ID,USER_ID) VALUES(%s,%s,%s)"
    cursor=conn.cursor(dictionary=True)

    for participant_id in participants_ids:
        id=str(uuid.uuid4())
        values=(id,chat_id,participant_id)
        cursor.execute(query,values)
    cursor.close()    

def find_direct_chat_btw_users(conn,sender_id:str,receiver_id:str):  
    query='''
SELECT chat_id FROM PARTICIPANTS
WHERE USER_ID IN (%s,%s) 
GROUP BY CHAT_ID
HAVING COUNT(DISTINCT USER_ID)=2
LIMIT 1
'''  
    values=(sender_id,receiver_id)
    cursor=conn.cursor(dictionary=True)
    cursor.execute(query,values)
    
    row=cursor.fetchone()
    
    cursor.close()

    if not row:
        return None
    
    
    return row["chat_id"]


    


    

def get_or_create_direct_chat(receiver_id:str,sender_id:str):
    try:
        conn=get_db_connection()

        existing_chat_id=find_direct_chat_btw_users(conn,receiver_id,sender_id)
        if existing_chat_id:
            conn.commit()
            return existing_chat_id
        
        new_chat_id=create_chat(conn)
        add_participants(conn,new_chat_id,[sender_id,receiver_id])

        conn.commit()
        conn.close()

        return new_chat_id

    except Exception as e:
        conn.rollback()
        raise e
    
def create_message(chat_id:str,content:str,sender_id:str):
    conn=get_db_connection()
    cursor=conn.cursor(dictionary=True)
    id=str(uuid.uuid4())
    query="INSERT INTO MESSAGES(ID,CONTENT,SENDER_ID,CHAT_ID,CREATED_AT) VALUES(%s,%s,%s,%s,NOW())"
    values=(id,content,sender_id,chat_id)

    cursor.execute(query,values)
    conn.commit()

    cursor.close()
    conn.close()    

    return id

def get_user_chat_ids(user_id:str):
    conn=get_db_connection()
    cursor=conn.cursor(dictionary=True)

    query="SELECT CHAT_ID FROM PARTICIPANTS WHERE USER_ID = %s"
    values=(user_id,)

    cursor.execute(query,values)
    rows=cursor.fetchall()
    conn.commit()

    cursor.close()
    conn.close()

    chat_ids=[]
    for row in rows:
        chat_ids.append(row["CHAT_ID"])
    return chat_ids

def get_other_participants(chat_id:str,user_id:str):
    conn=get_db_connection()
    cursor=conn.cursor(dictionary=True)

    query="SELECT * FROM PARTICIPANTS WHERE CHAT_ID=%s AND USER_ID!=%s"
    values=(chat_id,user_id)

    
    cursor.execute(query,values)
    row=cursor.fetchone()
    conn.commit()

    cursor.close()
    conn.close()

    if not row:
        return None
    user_id=row["user_id"]
    user=get_user_by_id(user_id)
    return {
        "user_id":user["id"],
        "username":user["username"]
    }

def get_last_msg(chat_id:str):
    conn=get_db_connection()
    cursor=conn.cursor(dictionary=True)

    query='''
SELECT * FROM MESSAGES WHERE CHAT_ID=%s ORDER BY CREATED_AT DESC LIMIT 1'''
    values=(chat_id,)

    cursor.execute(query,values)
    row = cursor.fetchone()
    conn.commit()

    cursor.close()
    conn.close()

    if not row:
        return None
    return {
        "content":row["content"],
        "created_at":row["created_at"]
    }

def get_chat_message(chat_id:str):
    conn=get_db_connection()
    cursor=conn.cursor(dictionary=True)

    query="SELECT * FROM MESSAGES WHERE CHAT_ID=%s ORDER BY CREATED_AT LIMIT 50"
    values=(chat_id,)

    cursor.execute(query,values)
    messages=cursor.fetchall()
    conn.commit()

    cursor.close()
    conn.close()

    return messages

def is_user_participants(chat_id:str,user_id:str):
    conn=get_db_connection()
    cursor=conn.cursor(dictionary=True)

    query="SELECT * FROM PARTICIPANTS WHERE CHAT_ID=%s AND USER_ID=%s LIMIT 1"
    values=(chat_id,user_id)

    cursor.execute(query,values)
    chats=cursor.fetchone()
    conn.commit()

    cursor.close()
    conn.close()

    if chats:
        return True
    else: 
        return False


    

