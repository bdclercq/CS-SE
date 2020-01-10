from sqlalchemy.sql import func

from project import db
from sqlalchemy.dialects.postgresql import HSTORE
from sqlalchemy.ext.mutable import MutableDict


class Keyvault(db.Model):

    __tablename__ = 'keyvault'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    key = db.Column(MutableDict.as_mutable(HSTORE))

    def __init__(self, user, key):
        self.key = {user: key}

    def to_json(self):
        return {
            'key': self.key
        }

    def get_key(self, user):
        '''This function should find the key for the given user in order to encrypt/decrypt messages.'''
        pass

    def encrypt(self, mess, user):
        key = self.get_key(user)
        '''Next the message should be encrypted'''
        pass

    def decrypt(self, mess, user):
        key = self.get_key(user)
        '''Next the message should be decrypted'''
        pass
