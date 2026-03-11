from flask import Flask,jsonify
from config.db import get_db_connection

app=Flask(__name__)


@app.route("/")
def home():
    return "Server Running..."


@app.route("/db")
def db():
    conn=get_db_connection()
    cursor=conn.cursor()

    query="SELECT * FROM users"
    cursor.execute(query)
    
    users=cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(users)
   
if __name__=="__main__":
    app.run(debug=True)