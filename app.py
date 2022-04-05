import json
from flask import Flask, jsonify, request

app = Flask(__name__)

contacts = []

@app.route("/add-data", methods = ["POST"])

def addTask():
    if not request.json :
        return jsonify(
            {
            "status" : "error"
            "message" : "Please Provide Data"
            }
        , 400)

    contact = {
        'id': contacts[-1]["id"] + 1,
        'Name' : request.json["Name"],
        'Contacts' : request.json.get("Contacts", ""),
        'Done' : False
    }

    contacts.append(contact)

    return jsonify(
        {
            "status" : "success",
            "message" : "Task Added Successfully"
        })

@app.route("/get-data")

def getContact() :
    return jsonify(
        {
          "data" : contacts
        })

if(__name__ == "__main__") :
    app.run(debug = True)