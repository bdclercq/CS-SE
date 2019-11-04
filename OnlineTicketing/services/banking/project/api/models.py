from sqlalchemy.sql import func

from project import db


class Banking(db.Model):
    __tablename__ = 'banking'

