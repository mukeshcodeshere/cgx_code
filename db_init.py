# db_init.py
from forex_python.converter import CurrencyRates
from datetime import datetime
from app import create_app, db
from app.models import CurrencyPair

app = create_app()

def fetch_currency_rates():
    c = CurrencyRates()
    # Get the latest currency rates for USD
    return c.get_rates('USD')

def clear_and_reset_database():
    # Drop all tables from the database
    db.drop_all()
    # Create all tables in the database
    db.create_all()

def populate_database():
    currency_rates = fetch_currency_rates()
    if not currency_rates:
        print("No currency rates fetched. Exiting.")
        return
    for currency, rate in currency_rates.items():
        # Split currency code into base and quote currencies
        base_currency = 'BTC'
        quote_currency = currency
        exchange_rate = rate
        #timestamp = datetime.utcnow()  # Get the current timestamp

        # Create a CurrencyPair object for each currency rate
        currency_pair = CurrencyPair(base_currency=base_currency, quote_currency=quote_currency, exchange_rate=exchange_rate)   #, timestamp=timestamp)
        db.session.add(currency_pair)

    # Commit the changes to the database
    db.session.commit()

    print("Database initialized successfully.")

if __name__ == "__main__":
    # with app.app_context():
    #     populate_database()
    
    with app.app_context():
        #clear_and_reset_database() # call this before populate if you want to reset db
        populate_database()

