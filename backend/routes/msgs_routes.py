from flask import Flask,Blueprint
from controllers.msg_controller import send_msg
from middleware.auth_middleware import jwt_required_custom

msgs_bp=Blueprint("messages",__name__)
msgs_bp.route("/",methods=["POST"])(jwt_required_custom(send_msg))

