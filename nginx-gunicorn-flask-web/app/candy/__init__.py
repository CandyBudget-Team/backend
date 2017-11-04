"""CandyBudget api module."""
import flask as fk
from candydb.common.core import setup_app
from candydb.common.models import UserModel
import os
import simplejson as json
import datetime
import traceback
from datetime import date, timedelta
from functools import update_wrapper
from calendar import monthrange
import time
import glob
import sys

# while True:
#     try:
#         # Flask app instance
#         app = setup_app(__name__)
#         break
#     except:
#         print("Connecting...")
#         traceback.print_exc(file=sys.stdout)
#         time.sleep(5)
app = setup_app(__name__)
# The api's version
API_VERSION = 0.1
# The candy base url
BASE_URL = '/candy/api/v{0}'.format(API_VERSION)

def candy_response(code, title, content):
    """Provides a common structure to represent the response
    from any api's endpoints.
        Returns:
            Flask response with a prettified json content.
    """
    import flask as fk
    response = {'code':code, 'title':title, 'content':content}
    return fk.Response(json.dumps(response, sort_keys=True, indent=4, separators=(',', ': ')), mimetype='application/json')

def data_pop(data=None, element=''):
    """Pop an element of a dictionary.
    """
    if data != None:
        try:
            del data[element]
        except:
            pass

def merge_dicts(*dict_args):
    """
    Given any number of dicts, shallow copy and merge into a new dict,
    precedence goes to key value pairs in latter dicts.
    """
    result = {}
    for dictionary in dict_args:
        result.update(dictionary)
    return result

# import all the candy endpoints.
import candy.endpoints
