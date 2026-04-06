from flask import Flask,request,jsonify,g
from models.msg_model import add_participants,create_chat,create_message,find_direct_chat_btw_users,get_or_create_direct_chat
from models.auth_model import get_user_by_id


def send_msg():
    try:
        req=request.json
        content=req.get("content")
        receiver_id=req.get("receiver_id")
        sender_id=g.get("user_id")
        

        if not content or not content.strip()  or not receiver_id:
            return jsonify({
                "success":False,
                "message":"missing required fields",
                "data":None
            }),400
        existing_user=get_user_by_id(receiver_id)
        

        if not existing_user:
            return jsonify({
                "success":False,
                "message":"receiver not found",
                "data":None
            }),400
        
        sender_id=g.get("user_id")

        if sender_id == receiver_id:
            return jsonify({
                "success":False,
                "message":"cannot send message to your self",
                "data":None
            }),400
        
        chat_id=get_or_create_direct_chat(receiver_id,sender_id)
        

        msg_id=create_message(chat_id,content,sender_id)

        return jsonify({
            "success":True,
            "message":"message sent successfully",
            "data":msg_id
        })
    except Exception as e:
        print(e)
        return jsonify({
            "success":False,
            "message":"unnexpected error occured",
            "data":None
        }),500
    
    


    
