#pip install flask
#pip install flask_pymongo

import os
import json
import datetime
from bson import json_util
from bson.objectid import ObjectId
from flask import Flask,request,jsonify
from flask_pymongo import pymongo


app = Flask(__name__)

CONNECTION_STRING = "mongodb+srv://saad:features@cluster0.hdo8c.mongodb.net/MongoExample1?retryWrites=true&w=majority"



client = pymongo.MongoClient(CONNECTION_STRING)
db = client.get_database('MongoExample1')
user_collection = pymongo.collection.Collection(db,'hello')



#test to insert data to the data base
@app.route("/insert")
def insert():
    db.collection.insert_one({"name": ["1","2"]})
    return ("Connected to the data base!")
        

@app.route("/find")
def find():
    data=db.consumers.find()
    print(data)
    for i in data:
        print(i)
    return ("Connected to the data base!")


app.run(debug=True,port=80)

