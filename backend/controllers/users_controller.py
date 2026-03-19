from flask import Flask,jsonify,request
from models.users_model import find_all_users

def get_users():
    try:
        users = find_all_users()
        print(users)

        if not users:
            return jsonify({
                "success":False,
                "message":"faild to get users",
                "data":None
            }),500
        
        return jsonify({
            "success":True,
            "message":"users fetch successfully",
            "data":users
        })
        
    except Exception:
        return jsonify({
            "success":False,
            "Message":"unnexpected error",
            "data":None
        })    