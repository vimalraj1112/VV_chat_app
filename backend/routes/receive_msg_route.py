from flask import Blueprint
from controllers.receive_controller import mark_delivered
from middleware.auth_middleware import jwt_required_custom

receive_msg_bp = Blueprint("receive_message", __name__)

@receive_msg_bp.route("/message/delivered", methods=["POST"])
@jwt_required_custom   # ✅ no ()
def delivered():
    return mark_delivered()