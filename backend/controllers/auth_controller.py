from flask import Flask,jsonify,request,make_response
from validators import email
from models.auth_model import create_user,get_user_by_email
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token
from datetime import timedelta

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
    
    result,user=create_user(name,email_id,password)
    if result == False:
        return jsonify({
            "success":False,
            "message":user,
            "data":None
        }),400
    
    token = create_access_token(
        identity=user["id"],          
        additional_claims={
            "name": user["username"],
            "email": user["email"]
        },
        expires_delta=timedelta(days=7)  
    ) 

    
    resp = make_response( jsonify({
        "success":True,
        "message":"Register successfully",
        "data":{
            "id":user['id'],
            "username":user["username"],
            "email":user["email"]
        }
    }))

    resp.set_cookie(
        "access_token",
        token,
        httponly=True,
        max_age=604800,
        secure=False,
        samesite='Lax'
    )
    
    return resp
    
    



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



    token = create_access_token(
        identity=user["id"],          
        additional_claims={
            "name": user["username"],
            "email": user["email"]
        },
        expires_delta=timedelta(days=7)  
    ) 

    
    resp = make_response( jsonify({
        "success":True,
        "message":"Login successfully",
        "data":{
            "id":user['id'],
            "username":user["username"],
            "email":user["email"]
        }
    }))

    resp.set_cookie(
        "access_token",
        token,
        httponly=True,
        max_age=604800,
        secure=False,
        samesite='Lax'
    )
    return resp

def logout_user():
    resp = make_response(jsonify({
        "success":True,
        "message":"logout successfully",
        "data":None
    }))
    resp.set_cookie(
        "access_token",
        ""
        
    )
    return resp


    

    




