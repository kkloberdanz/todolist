from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import uuid


app = Flask(__name__)
CORS(app)


data = [
    {
        'id': 1,
        'title': "Todo One",
        'completed': False
    },
    {
        'id': 2,
        'title': "Todo Two",
        'completed': False
    },
    {
        'id': 3,
        'title': "Todo Three",
        'completed': False
    },
]


@app.route("/todos", methods=['POST', 'GET', 'DELETE'])
def todos():
    if request.method == 'GET':
        pass

    elif request.method == 'POST':
        content = request.json
        _id = str(uuid.uuid4())
        content['id'] = _id
        data.append(content)

    else:
        return (400, f'invalid method: {request.method}')

    print(data)
    return jsonify(data)


@app.route("/todos/<this_id>", methods=['POST', 'GET', 'DELETE'])
def todo_id(this_id):
    global data
    if request.method == 'GET':
        for obj in data:
            if obj['id'] == this_id:
                return jsonify(obj)
            return jsonify({})
    elif request.method == 'DELETE':
        l = [obj for obj in data if str(obj['id']) != this_id]
        data = l
    else:
        return (400, f'invalid method: {request.method}')
    print(data)
    return jsonify(data)


if __name__ == "__main__":
    app.run()
