from flask import Flask
from config.db import get_db_connection


def mark_as_delivered(message_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    query = "UPDATE MESSAGES SET status='delivered' WHERE ID=%s"
    cursor.execute(query, (message_id,))
    conn.commit()

    cursor.close()
    conn.close()

    return message_id