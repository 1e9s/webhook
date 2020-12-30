import os
import json

from flask import Flask
from flask import request
from flask import render_template
from views import get_wrapup, post_wrapup

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/onwrapup/', methods=['GET', 'POST'])
def onwrapup():
    if request.method == 'GET':
        return get_wrapup(request)
    else:
        return post_wrapup(request)

@app.route('/onwrapup/payload/')
def onwrapup_payload():
    PROJ_DIR = os.path.realpath(os.path.dirname(__file__))
    filepath = os.path.join(PROJ_DIR, 'lastpost.json')
    with open(filepath, 'r') as f: payload = json.load(f)
    data = {
        'payload': payload
    }
    return render_template('wrapup.html', data=data)


if __name__ == '__main__':
    app.run()

