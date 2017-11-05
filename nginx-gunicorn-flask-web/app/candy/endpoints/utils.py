import simplejson as json
import requests
import numpy

def agregated(feature='amount', transactions=[]):
    if len(transactions) == 0:
        return 0
    else:
        return sum(t[feature] for t in transactions)

def query_transactions(customer_id=None, current_date=None):
    data = {'budget':0, 'spending':0, 'balance':0, 'savings':0, 'saving-rank':0, 'reward-rank':0}
    url = "https://3hkaob4gkc.execute-api.us-east-1.amazonaws.com/prod/au-hackathon/transactions"
    if customer_id is None or current_date is None:
        return data
    try:
        payload = {"customer_id": int(customer_id), "date_to":current_date}
        body = json.dumps(payload)
        request = requests.post(url, data=body)
        response = request.json()
        transactions_list = response[0]["customers"][0]['transactions']
        total_transactions = agregated(feature='amount', transactions=transactions_list)
        total_rewards = agregated(feature='rewards_earned', transactions=transactions_list)

        data["spending"]=total_transactions
        data["rewards"]=total_rewards

        print(data)
    except:
        pass
    return data
