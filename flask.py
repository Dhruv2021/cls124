from flask import Flask,jsonify,request

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'name': u'Dhruv',
        'contact': u'8700963875', 
        'done': False
    },
    {
        'id': 2,
        'name': u'Dhruv',
        'contact': u'8826235010', 
        'done': False
    }
]

@app.route("/")
def helloworld():
    return "hello world"

@app.route("/get-data")
def gettask():
    return jsonify({
        "data":tasks
    }) 

@app.route("/add-data",methods=["POST"])
def addtask():
    if not request.json:
        return jsonify({
            
            "status":"error",
            "message":"please provide the data"
        },400)
    task={
        'id': tasks[-1]['id'] + 1,
        'name': request.json['name'],
        'contact': request.json.get('contact', ""),
        'done': False
    }
    tasks.append(task)
        
    return jsonify({
            
        "status":"success",
        "message":"Task Added"
    })




if __name__=="__main__":
    app.run(debug=True)