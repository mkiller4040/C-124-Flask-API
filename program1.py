
from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = []

@app.route("/adddata", methods = ["POST"])

def addtask() :
    if not request.json :
        return jsonify(
        {
            "status" : "error",
            "message" : "Please Provide Data"
        }
        ,400)

    task = {
        "id" : tasks[-1]["id"] + 1,
        "title" : request.json["title"],
        "done" : False
    }

    tasks.append(task)

    return jsonify(
    {
      "status" : "success",
      "message" : "Task Added Successfully"
    })

@app.route("/getdata")

def getTask() :
    return jsonify(
        {
          "data" : tasks
        })

if(__name__ == "__main__") :
    app.run(debug = True)