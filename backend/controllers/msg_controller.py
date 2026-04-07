from flask import Flask,request,jsonify,g
from models.msg_model import add_participants,create_chat,create_message,find_direct_chat_btw_users,get_or_create_direct_chat,get_user_chat_ids,get_other_participants,get_last_msg,is_user_participants,get_chat_message
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
    

def get_chats():
    try:
        user_id=g.get("user_id")
        print(user_id)
        chat_ids:list[str]=get_user_chat_ids(user_id)
        print(chat_ids)
        chats:list[dict]=[]
        for chat_id in chat_ids:
            other_user=get_other_participants(chat_id,user_id)
            last_msg=get_last_msg(chat_id)
            chats.append({
                "chat_id":chat_id,
                "user_id":other_user["user_id"],
                "username":other_user["username"],
                "last_message":last_msg["content"],
                "last_message_at":last_msg["created_at"]
            })
        return jsonify({
            "success":True,
            "message":"chat fetch successfully",
            "data":chats
        })

        
       
        


    
    except Exception as e:
        print(e)
        return jsonify({
            "success":False,
            "message":"unnexpected error",
            "data":None
        }),500
    
def get_msgs(chat_id):
    try:
        user_id=g.get("user_id")
        is_participants=is_user_participants(chat_id,user_id)
        if not is_participants:
            return jsonify({
                "success":False,
                "message":"forbidden",
                "data":None
            }),403
        messages=get_chat_message(chat_id)
        return jsonify({
            "success":True,
            "message":"fetch successfully",
            "data":messages
        })

    except Exception as e:
        print(e)
        return jsonify({
            "success":False,
            "message":"unnexpected error",
            "data":None
        }),500


           