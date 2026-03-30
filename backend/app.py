from flask import Flask,jsonify
from config.db import get_db_connection
from dotenv import load_dotenv
import os
from routes.auth_route import auth_bp
from flask_jwt_extended import JWTManager
from routes.user_route import users_bp
from flask_cors import CORS



app=Flask(__name__)
CORS(app,
     origins=['*'],
         supports_credentials=True)

app.config["JWT_SECRET_KEY"]=os.getenv("JWT_SECRET_KEY")
app.config["JWT_TOKEN_LOCATION"] = ["cookies"]
app.config["JWT_ACCESS_COOKIE_NAME"] = "access_token"

jwt = JWTManager(app)


app.register_blueprint(auth_bp,url_prefix="/auth")
app.register_blueprint(users_bp,url_prefix="/users")




@app.route("/")
def home():
    return jsonify({
        "name":"VV_ChatApp"
    })
   
if __name__=="__main__":
    app.run(debug=True)