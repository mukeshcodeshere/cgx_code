# app/models.py
from . import db

class CurrencyPair(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    base_currency = db.Column(db.String(10), nullable=False)
    quote_currency = db.Column(db.String(10), nullable=False)
    exchange_rate = db.Column(db.Float, nullable=False)
