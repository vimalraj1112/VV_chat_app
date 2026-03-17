from flask import Flask,jsonify
from config.db import get_db_connection
from dotenv import load_dotenv
import os
from routes.auth_route import auth_bp
from flask_jwt_extended import JWTManager



app=Flask(__name__)

app.config["JWT_SECRET_KEY"]=os.getenv("JWT_SECRET_KEY")

jwt = JWTManager(app)


app.register_blueprint(auth_bp,url_prefix="/auth")




@app.route("/")
def home():
    return "VV_chat Running..."
   
if __name__=="__main__":
    app.run(debug=True)