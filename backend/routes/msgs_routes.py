from flask import Flask,Blueprint
from controllers.msg_controller import send_msg,get_chats,get_msgs
from middleware.auth_middleware import jwt_required_custom

msgs_bp=Blueprint("messages",__name__)
msgs_bp.route("/",methods=["POST"])(jwt_required_custom(send_msg))
msgs_bp.route("/",methods=["GET"])(jwt_required_custom(get_chats))
msgs_bp.route("/<chat_id>",methods=["GET"])(jwt_required_custom(get_msgs))



