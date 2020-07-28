from flask import Flask, render_template, url_for, redirect, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_heroku import Heroku



app = Flask(__name__)
heroku = Heroku(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/enter_command', methods=['POST'])
def enter_command():
    return "test"


if __name__ == "__main__":
    app.debug = True
    app.run()
