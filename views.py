import os
import json

from flask import render_template

def get_wrapup(request):
    if request.remote_addr == '128.199.71.30':
        return "<secret>"
    else:
        return "UNAUTHORIZED REQUEST"


def post_wrapup(request):
    data = request.form.to_dict()

    PROJ_DIR = os.path.realpath(os.path.dirname(__file__))
    filepath = os.path.join(PROJ_DIR, 'lastpost.json')
    with open(filepath, 'w') as f: json.dump(data, f)

    return data

    # data = {
    #     'payload': request.POST
    # }
    # return render_template('wrapup.html', data=data)

