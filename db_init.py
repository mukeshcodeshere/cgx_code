# db_init.py
from app import create_app, db
from app.models import CurrencyPair
from forex_python.converter import CurrencyRates, RatesNotAvailableError

app = create_app()
c = CurrencyRates()
with app.app_context():
    db.create_all()

    # Sample currency pairs
    btc_usdt = CurrencyPair(base_currency='EURO', quote_currency='USDT', exchange_rate=c.get_rate('USD', 'EUR'))
    eth_usdt = CurrencyPair(base_currency='GBP', quote_currency='USDT', exchange_rate=c.get_rate('USD', 'GBP'))
    btc_usdc = CurrencyPair(base_currency='YEN', quote_currency='USDT', exchange_rate=c.get_rate('USD', 'JPY'))
    eth_usdc = CurrencyPair(base_currency='YUAN', quote_currency='USDT', exchange_rate=c.get_rate('USD', 'CNY'))

    # Add the currency pairs to the session
    db.session.add(btc_usdt)
    db.session.add(eth_usdt)
    db.session.add(btc_usdc)
    db.session.add(eth_usdc)

    # Commit the changes to the database
    db.session.commit()

    print("Database initialized successfully.")
