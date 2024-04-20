# app/models.py
from . import db


class CurrencyPair(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    base_currency = db.Column(db.String(10), nullable=False)
    quote_currency = db.Column(db.String(10), nullable=False)
    exchange_rate = db.Column(db.Float, nullable=False)

# from datetime import datetime
# class CurrencyPair(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     base_currency = db.Column(db.String(10), nullable=False)
#     quote_currency = db.Column(db.String(10), nullable=False)
#     exchange_rate = db.Column(db.Float, nullable=False)
#     timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)  # Add timestamp field

#     def __repr__(self):
#         return f"CurrencyPair('{self.base_currency}', '{self.quote_currency}', {self.exchange_rate}, {self.timestamp})"
