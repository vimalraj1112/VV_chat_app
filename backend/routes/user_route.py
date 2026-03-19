from flask import Flask,Blueprint
from controllers.users_controller import get_users
from middleware.auth_middleware import jwt_required_custom

users_bp=Blueprint("users",__name__)

users_bp.route("/users",methods=["GET"])(jwt_required_custom(get_users))  