import datetime
from ..core import db
import json
import hashlib
import time

class UserModel(db.Document):
    """CandyBudget backend user model.
    The model holding the user information.

    Attributes:
        created_at: A string value of the creation timestamp.
        account_id: A string value of the user email.
    """
    created_at = db.StringField(default=str(datetime.datetime.utcnow()))
    connected_at = db.StringField(default=str(datetime.datetime.utcnow()))
    account_id = db.StringField(required=True, unique=True)

    def get_id(self):
        """Get the user id properly
        Returns:
            The user object id.
        """
        try:
            return unicode(self.id)
        except NameError:
            return str(self.id)

    def save(self, *args, **kwargs):
        """Overwrite the user mongoengine save
        Returns:
            The call to the mongoengine Document save function.
        """
        if not self.created_at:
            self.created_at = str(datetime.datetime.utcnow())
        return super(UserModel, self).save(*args, **kwargs)

    def info(self):
        """Build a dictionary structure of an user model instance content.
        Returns:
            The dictionary content of the user model.
        """
        data = {'created':str(self.created_at), 
        'id': str(self.id), 'account-id' : self.account_id}
        return data

    def to_json(self):
        """Transform the extended dictionary into a pretty json.
        Returns:
            The pretty json of the extended dictionary.
        """
        data = self.info()
        return json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))


            
