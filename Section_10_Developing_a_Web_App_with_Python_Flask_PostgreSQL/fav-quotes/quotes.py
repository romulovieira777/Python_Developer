from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return '<h1> Hello World</h1>'

@app.route('/about')
def about():
    return '<h1>Hello World from about page</h1>'

@app.route('/quotes')
def quotes():
    return '<h1>Life is journey</h1>'
