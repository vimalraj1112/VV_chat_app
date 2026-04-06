from functools import wraps
from flask_jwt_extended import verify_jwt_in_request,get_jwt_identity
from flask import Flask,request,jsonify,g






def jwt_required_custom(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            
            verify_jwt_in_request()
            
            
            g.user_id=get_jwt_identity()
        
            

        except Exception as e:
            print(e)
            g.user_id=None
            return jsonify({
                "success":False,
                "message":"token missing or invalid",
                "data":None
            }),401
        return fn(*args, **kwargs)
        

    return wrapper

           