import json

from ..core import db

class MonthSummary(db.EmbeddedDocument):
    year = db.IntField(required=True)
    month = db.IntField(required=True)
    budget = db.FloatField(required=True)
    spending = db.FloatField(required=True)
    rewards = db.FloatField(required=True)
    payment = db.FloatField(required=True)
    # The savings accumulated from previous months
    savings = db.FloatField(required=True)
    # Rank of this month
    saving_rank = db.IntField(required=True)
    # Rank of this month
    reward_rank = db.IntField(required=True)

    def info(self):
        data = {
            "year": self.year,
            "month": self.month,
            "budget": self.budget,
            "spending": self.spending,
            "rewards": self.rewards,
            "payment": self.payment,
            "savings": self.savings,
            "saving_rank": self.saving_rank,
            "reward_rank": self.reward_rank,
        }
        return data

    def to_json(self):
        data = self.info()
        return json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))

class Customer(db.Document):
    account_id = db.LongField(required=True)
    customer_id = db.LongField(required=True)
    summaries = db.ListField(db.EmbeddedDocumentField(MonthSummary))

    def info(self):
        data = {
            "account_id": self.account_id,
            "customer_id": self.customer_id,
            "summaries": [b.info() for b in self.summaries],
        }
        return data

    def to_json(self):
        data = self.info()
        return json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))
