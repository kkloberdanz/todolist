from flask import Flask
from flask_cors import CORS
from flask import jsonify


app = Flask(__name__)
CORS(app)


@app.route("/todos")
def hello():
    dct = [
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
    return jsonify(dct)


if __name__ == "__main__":
    app.run()
