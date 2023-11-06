# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to My Simple Flask Website"

@app.route('/about')
def about():
    return "This is the About Page"

if __name__ == '__main__':
    app.run(debug=True)
