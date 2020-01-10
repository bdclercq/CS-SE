from sqlalchemy.sql import func

from project import db


class Banking(db.Model):
    __tablename__ = 'banking'

    def __init__(self, kv=None):
        self.initialized = True
        self.kv = kv
