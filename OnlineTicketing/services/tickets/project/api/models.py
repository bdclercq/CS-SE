from project import db
from sqlalchemy.sql import func


class Ticket(db.Model):
    __tablename__ = 'tickets'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    amount = db.Column(db.Integer, default=1000000, nullable=False)
    unit_price = db.Column(db.Float, default=56.99, nullable=False)
    period_from = db.Column(db.DateTime, default=func.now(), nullable=False)
    period_to = db.Column(db.DateTime, default=func.now(), nullable=False)

    def __init__(self, amount, unit_price, period_from, period_to):
        self.amount = amount
        self.unit_price = unit_price
        self.period_from = period_from
        self.period_to = period_to

    def to_json(self):
        return {
            'amount': self.amount,
            'price': self.unit_price,
            'from': self.period_from,
            'until': self.period_to
        }
