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


id="5fc69d8b03a2491e64c7fbd2"
app = Flask(__name__)

CONNECTION_STRING = "mongodb+srv://yolo:yolo@cluster0.q4imu.mongodb.net/<dbname>?retryWrites=true&w=majority"



client = pymongo.MongoClient(CONNECTION_STRING)
db = client.get_database('<dbname>')





@app.route("/pushNoti",methods=["GET","POST"])
def pushNoti():
    members=[]
    memberIds=[]
    tokens=[]
    events = db.events.find_one({'_id':bson.ObjectId(id)})
    members=events["members"]
    
    for i in members:
        memberIds.append(i["userId"])

    for i in memberIds:
        member=db.users.find_one({"_id":bson.ObjectId(str(i))})
        if(len(member["token"])>0):
            tokens.append(member["token"])

    print(tokens)
        
    return Response("Success", status=201)

app.run(debug=True,port=80)

