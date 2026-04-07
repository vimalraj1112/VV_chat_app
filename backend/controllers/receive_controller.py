from flask import Flask,request,jsonify
from models.receive_model import mark_as_delivered

def mark_delivered():
    try:
        req = request.json
        message_id = req.get("message_id")

        if not message_id:
            return jsonify({
                "success": False,
                'message':'not delivered',
                'data':None}), 400

        mark_as_delivered(message_id)

        return jsonify({
            "success": True,
            "message": "message delivered",
            'data':message_id
        })

    except Exception as e:
        print(e)
        return jsonify({"success": False}), 500  
      