from flask import Flask, render_template, url_for, request
# from models import db


app = Flask(__name__)

@app.route('/<string:username>')
@app.route('/')
def defaultpage(name=None):
    return render_template('index.html')



