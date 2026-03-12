from flask import Flask,jsonify
from config.db import get_db_connection
from dotenv import load_dotenv
import os
from routes.auth_route import auth_bp


app=Flask(__name__)

app.register_blueprint(auth_bp,url_prefix="/auth")



@app.route("/")
def home():
    return "VV_chat Running..."
   
if __name__=="__main__":
    app.run(debug=True)