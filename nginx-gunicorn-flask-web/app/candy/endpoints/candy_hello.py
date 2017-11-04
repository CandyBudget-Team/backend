import json

from flask_api import status
import flask as fk

from candydb.common import crossdomain
from candy import app, BASE_URL, candy_response, data_pop, merge_dicts
from candydb.common.models import UserModel

import mimetypes
import simplejson as json
import traceback
import datetime
import random
import string
import os
import _thread

@app.route(BASE_URL + '/public/hello', methods=['GET','POST','PUT','UPDATE','DELETE','POST'])
@crossdomain(fk=fk, app=app, origin='*')
def public_candy_hello():
    if fk.request.method == 'GET':
        # Maybe perform some sanity checks
        return candy_response(200, 'API reached', 'The CandyBudget API instance is up and running')
    else:
        return candy_response(405, 'Method not allowed', 'This endpoint supports only a GET method.')