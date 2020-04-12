from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import uuid


app = Flask(__name__)
CORS(app)


def new_id():
    return uuid.uuid4()


data = [
    {
        'id': new_id(),
        'title': "Todo One",
        'completed': False
    },
    {
        'id': new_id(),
        'title': "Todo Two",
        'completed': False
    },
    {
        'id': new_id(),
        'title': "Todo Three",
        'completed': False
    },
]


@app.route("/todos", methods=['POST', 'GET'])
def todos():
    if request.method == 'GET':
        pass

    elif request.method == 'POST':
        content = request.json
        _id = new_id()
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
        data = [obj for obj in data if str(obj['id']) != this_id]
        return this_id
    else:
        return (400, f'invalid method: {request.method}')
    print(data)
    return jsonify(data)


if __name__ == "__main__":
    app.run()
