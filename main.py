from flask import Flask
from flask import jsonify

app = Flask(__name__)


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'I like to make Apps!!!!!!'


@app.route('/name/<value>')
def name(value):
    val = {"value": value}
    return jsonify(val)


@app.route('/my')
def html():
    """Returns some custom HTML"""
    return """
    <title>HTML Page</title>
    <p><b>Hello!!! Welcome to my HTML page : ) </b></p>
    """


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
