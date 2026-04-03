from flask import Flask,json
from config.db import get_db_connection
import uuid


def create_conversation(participants:list,content:str):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    conversation_id = uuid()

    sorted_participant = json.dumps(sorted(participants))

    last_msg=content
    
    querry ="INSERT INTO CONVERSATION(ID,PARTICIPANTS,LAST_MESSAGE,LAST_MESSAGE_AT) VALUES(%s,%s,%s,NOW())"
    values =(conversation_id,sorted_participant,last_msg)

    cursor.execute(querry,values)
    conn.commit()

    cursor.close()
    conn.close()

    return conversation_id

def find_conversation_by_participants(participants:list):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    sorted_participants =sorted(participants)

    querry ="SELECT * FROM CONVERSATIONS WHERE JSON_CONTAINS(PARTICIPANTS,JSON_ARRAY(%s,%s)) AND JSON_LENGHT(PARTICIPANTS)=%d LIMIT 1"
    values =(participants[0],participants[1],len(participants))

    conversation = cursor.execute(querry,values)
    conn.commit()

    cursor.close()
    conn.close()

    return conversation

