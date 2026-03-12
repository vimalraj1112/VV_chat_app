from flask import Flask,jsonify,request

def register_user():

    data= request.json

    name=data.get("name")
    email=data.get("email")
    password=data.get("password")

    if not name or not email or not password:
        return jsonify({
            "success":False,
            "message":"Missing Requirements",
            "data":None

        }),400
    
    return jsonify({
        "seccess":True,
        "message":"User Register Successfully",
        "data":data
    }),201
    return data

