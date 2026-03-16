from flask import Flask,jsonify,request
from validators import email
from models.auth_model import create_user,get_user_by_email
from werkzeug.security import check_password_hash

def register_user():

    data= request.json

    name=data.get("name")
    email_id=data.get("email")
    password=data.get("password")

    if not email_id or not name or not password:
        return jsonify({
            "success":False,
            "message":"Missing required field",
            "data":None
        }),400

    if not email(email_id) or len(name)<=3 or len(password)>8:
        return jsonify({
            "success":False,
            "message":"Invalid credentials",
            "data":None
        }),400
    

    if not name or not email_id or not password:
        return jsonify({
            "success":False,
            "message":"Missing Requirements",
            "data":None

        }),400
    
    result,message=create_user(name,email_id,password)
    if result == False:
        return jsonify({
            "success":False,
            "message":message,
            "data":None
        }),400
    
    
    return jsonify({
        "success":True,
        "message":"User Register Successfully",
        "data":message
    }),201

def login_user():

    data = request.json

    email_id=data.get("email")
    password=data.get("password")

    if not email_id or not password:
        return jsonify({
            "success":False,
            "message":"missing requirements",
            "data":None
        }),400
    
    if not email(email_id):
        return jsonify({
            "success":False,
            "message":"Invalid Credential",
            "data":None
        }),400
    
    user = get_user_by_email(email_id)

    if not user:
        return jsonify({
            "success":False,
            "message":"user not found",
            "data":None
        }),404
    

    is_val_pass= check_password_hash(user["password"],password) 

    if not is_val_pass:
        return jsonify({
            "success":False,
            "message":"invalid credential",
            "data":None
        })  
    
    return jsonify({
        "success":True,
        "message":"Login successfully",
        "data":{
            "id":user['id'],
            "username":user["username"],
            "email":user["email"]
        }
    })
    

    




