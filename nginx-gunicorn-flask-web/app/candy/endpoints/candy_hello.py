import json

from flask_api import status
import flask as fk

from candydb.common import crossdomain
from candy import app, BASE_URL, candy_response, data_pop, merge_dicts
from candydb.common.models import Customer, MonthSummary

import mimetypes
import simplejson as json
import traceback
import datetime
import random
import string
import os
import _thread
from .utils import *

@app.route(BASE_URL + '/public/hello', methods=['GET','POST','PUT','UPDATE','DELETE','POST'])
@crossdomain(fk=fk, app=app, origin='*')
def public_candy_hello():
    if fk.request.method == 'GET':
        # Maybe perform some sanity checks
        return candy_response(200, 'API reached', 'The CandyBudget API instance is up and running')
    else:
        return candy_response(405, 'Method not allowed', 'This endpoint supports only a GET method.')

@app.route(BASE_URL + '/budget', methods=['GET','POST','PUT','UPDATE','DELETE','POST'])
@crossdomain(fk=fk, app=app, origin='*')
def history_budget():
    if fk.request.method == 'POST':
        if fk.request.data:
            try:
                payload = json.loads(fk.request.data)
                account_id = payload.get('account-id', None)
                customer_id = payload.get('customer-id', None)
                if account_id and customer_id:
                    customers = [Customer.objects(account_id=account_id, customer_id=customer_id).first()]
                elif account_id and customer_id is None:
                    customers = Customer.objects(account_id=account_id)
                elif account_id is None and customer_id:
                    customers = [Customer.objects(customer_id=customer_id).first()]
                else:
                    customers = Customer.objects()
            except:
                customers = Customer.objects()
        else:
           customers = Customer.objects()

        data = {'size':len(customers), 'budgets':[customer.info() for customer in customers if customer]}
        return candy_response(200, 'Budgets', data)
    else:
        return candy_response(405, 'Method not allowed', 'This endpoint supports only a POST method.')

@app.route(BASE_URL + '/spending', methods=['GET','POST','PUT','UPDATE','DELETE','POST'])
@crossdomain(fk=fk, app=app, origin='*')
def current_spending():
    if fk.request.method == 'POST':
        if fk.request.data:
            try:
                payload = json.loads(fk.request.data)
                current_date = payload.get('current-date', None)
                customer_id = payload.get('customer-id', None)
                agregated = query_transactions(customer_id, current_date)
                if current_date and customer_id:
                    customer = Customer.objects(customer_id=customer_id).first()
                    current_month = None
                    for summary in customer.summaries:
                        month_day_year = current_date.split("/")
                        if "{0}/{1}".format(summary.month, summary.year) == "{0}/{1}".format(month_day_year[0], month_day_year[2]):
                            current_month = summary
                            break
                    if current_month:
                        agregated['budget'] = current_month.budget
                        agregated['balance'] = agregated['budget'] - agregated['spending']
                        agregated['savings'] = current_month.savings
                        agregated['saving-rank'] = current_month.saving_rank
                        agregated['reward-rank'] = current_month.reward_rank
                    return candy_response(200, 'Budgets', agregated)
                else:
                    return candy_response(404, 'Unknown customer or date.', agregated)
            except:
                return candy_response(500, 'Error in the payload.', query_transactions(None))
        else:
           return candy_response(500, 'Customer id and current date required.', query_transactions(None))
    else:
        return candy_response(405, 'Method not allowed', 'This endpoint supports only a GET method.')


