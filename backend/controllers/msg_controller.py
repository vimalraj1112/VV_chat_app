from flask import Flask,jsonify,g,request
from models.msg_model import create_conversation,find_conversation_by_participants




def send_msg():
    try:

        data = request.json

        content = data.get("content")
        conversation_id = data.get("conversation_id")
        reciever_id = data.get("reciever_id")

        if not content or not reciever_id:
            return jsonify({
                "success":False,
                "message":"missing required fields",
                "data":None
            })  
        
        if not conversation_id:
            
            sender_id = g.user_id
            participants = [sender_id,reciever_id]
            existing_conversation = find_conversation_by_participants(participants)
            
                
            conversation_id=create_conversation(participants,content)


            

            
    
    except Exception as e:
        return jsonify({
            "success":False,
            "message":"unexpected error",
            "data":None
        })
    
    