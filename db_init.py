# db_init.py
from app import create_app, db
from app.models import CurrencyPair

app = create_app()

with app.app_context():
    db.create_all()

    # Sample currency pairs
    btc_usdt = CurrencyPair(base_currency='bitcoin', quote_currency='usdt', exchange_rate=50000.0)
    eth_usdt = CurrencyPair(base_currency='ethereum', quote_currency='usdt', exchange_rate=2000.0)
    btc_usdc = CurrencyPair(base_currency='bitcoin', quote_currency='usdc', exchange_rate=50000.0)
    eth_usdc = CurrencyPair(base_currency='ethereum', quote_currency='usdc', exchange_rate=2000.0)

    # Add the currency pairs to the session
    db.session.add(btc_usdt)
    db.session.add(eth_usdt)
    db.session.add(btc_usdc)
    db.session.add(eth_usdc)

    # Commit the changes to the database
    db.session.commit()

    print("Database initialized successfully.")
