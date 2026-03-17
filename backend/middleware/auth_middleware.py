from functools import wraps
from flask_jwt_extended import verify_jwt_in_request,get_jwt
from flask import Flask,request,jsonify



def jwt_required_custom(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            verify_jwt_in_request(locations=["cookies"], cookie_name="access_token")
        except Exception:
            return jsonify({
                "success":False,
                "message":"token missing or invalid",
                "data":None
            })
        return fn(*args, **kwargs)
        

    return wrapper

           