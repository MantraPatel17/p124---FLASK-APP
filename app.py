from flask import Flask, jsonify, request

app = Flask(__name__)

data = [
    {
        'Contact': "9987644456",
        "Name": "Raju",
        "done": False,
        "id": 1
    },
    {
        "Contact": "9876543222",
        "Name": "Rahul",
        "done": False,
        "id": 2
    }

]


@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "Please provide the task!"
        }, 400)

    task = {
        'id': data[-1]['id']+1,
        'Name': request.json['Name'],
        'Contact': request.json.get('Contact', ""),
        'done': False,
    }

    data.append(task)

    return jsonify({
        "status": "success",
        "message": "task added successfully!!!!!!!!!!!!!!!!!!!!!!!!"
    })


@app.route("/get-data")
def get_task():
    return jsonify({
        "data": data
    })


if __name__ == '__main__':
    app.run()
