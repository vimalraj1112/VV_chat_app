from flask import Flask,jsonify,request
from validators import email
from models.auth_model import create_user

def register_user():

    data= request.json

    name=data.get("name")
    email_id=data.get("email")
    password=data.get("password")

    if not email(email_id) or len(name)<=3 or len(password)>8:
        return jsonify({
            "success":False,
            "message":"Invalid credentials",
            "data":None
        })
    
    

    

    if not name or not email_id or not password:
        return jsonify({
            "success":False,
            "message":"Missing Requirements",
            "data":None

        }),400
    
    result=create_user(name,email_id,password)
    
    
    return jsonify({
        "success":True,
        "message":"User Register Successfully",
        "data":result
    }),201
    

    




