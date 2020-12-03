#pip install flask
#pip install flask_pymongo

import os
import json
import datetime
import bson
from bson import json_util
from bson.objectid import ObjectId
from flask import Flask,request,jsonify,Response
from flask_pymongo import pymongo
from pyfcm import FCMNotification 



app = Flask(__name__)

CONNECTION_STRING = "mongodb+srv://yolo:yolo@cluster0.q4imu.mongodb.net/<dbname>?retryWrites=true&w=majority"



client = pymongo.MongoClient(CONNECTION_STRING)
db = client.get_database('<dbname>')

push_service=FCMNotification(api_key="AAAAIBuM_1E:APA91bGii9bBRWYtiCGdw9zu55pAy_WkQ23Vdj7lv3fsbgU7I6EIrhzNSxxI9_3mPQsLfJOYuZcZ6BGgg5_CUHlCeHNLA_qLJ0YJWfXhCuMonm5AJIvFNrbbg-OilwdmQ1XWQEdH4RBx")

@app.route("/",methods=["GET","POST"])
def index():
    return Response("Working", status=201)


@app.route("/pushNoti",methods=["GET","POST"])
def pushNoti():
    if request.method == "POST":
        print(request.json["eventId"])
        print(request.json["date"])
        eventId=request.json["eventId"]
        members=[]
        memberIds=[]
        tokens=[]
        events = db.events.find_one({'_id':bson.ObjectId(eventId)})
        members=events["members"]

        for i in members:
            memberIds.append(i["userId"])

        for i in memberIds:
            member=db.users.find_one({"_id":bson.ObjectId(str(i))})
            if(len(member["token"])>0):
                tokens.append(member["token"])

        print(tokens)
        message_title=request.json["name"]
        message_body="Reminder You have an upcoming event at "+request.json["date"]
        result = push_service.notify_multiple_devices(registration_ids=tokens,message_title=message_title,
                                                            message_body=message_body,
                                                            sound="default")

        print(result)
    return Response("Success", status=201)

if __name__=="__main__":
    app.run(debug=True)

