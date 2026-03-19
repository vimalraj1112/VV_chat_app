from flask import Flask,request,jsonify,Blueprint
from controllers.auth_controller import register_user,login_user,logout_user
from middleware.auth_middleware import jwt_required_custom


auth_bp=Blueprint("auth",__name__)
auth_bp.route("/register",methods=["POST"])(register_user)
auth_bp.route("/login",methods=["POST"])(login_user)
auth_bp.route("/logout",methods=["POST"])(logout_user)





    

