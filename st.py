import streamlit as st
from forex_python.converter import CurrencyRates
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

instrument_array = [
            "AED",
            "AFN",
            "ALL",
            "AMD",
            "ANG",
            "AOA",
            "ARS",
            "AUD",
            "AWG",
            "AZN",
            "BAM",
            "BBD",
            "BDT",
            "BGN",
            "BHD",
            "BIF",
            "BMD",
            "BND",
            "BOB",
            "BRL",
            "BSD",
            "BTC",
            "BTN",
            "BWP",
            "BYN",
            "BYR",
            "BZD",
            "CAD",
            "CDF",
            "CHF",
            "CLF",
            "CLP",
            "CNH",
            "CNY",
            "COP",
            "CRC",
            "CUC",
            "CUP",
            "CVE",
            "CZK",
            "DJF",
            "DKK",
            "DOP",
            "DZD",
            "EGP",
            "ERN",
            "ETB",
            "EUR",
            "FJD",
            "FKP",
            "GBP",
            "GEL",
            "GGP",
            "GHS",
            "GIP",
            "GMD",
            "GNF",
            "GTQ",
            "GYD",
            "HKD",
            "HNL",
            "HRK",
            "HTG",
            "HUF",
            "IDR",
            "ILS",
            "IMP",
            "INR",
            "IQD",
            "IRR",
            "ISK",
            "JEP",
            "JMD",
            "JOD",
            "JPY",
            "KES",
            "KGS",
            "KHR",
            "KMF",
            "KPW",
            "KRW",
            "KWD",
            "KYD",
            "KZT",
            "LAK",
            "LBP",
            "LKR",
            "LRD",
            "LSL",
            "LYD",
            "MAD",
            "MDL",
            "MGA",
            "MKD",
            "MMK",
            "MNT",
            "MOP",
            "MRO",
            "MUR",
            "MVR",
            "MWK",
            "MXN",
            "MYR",
            "MZN",
            "NAD",
            "NGN",
            "NIO",
            "NOK",
            "NPR",
            "NZD",
            "OMR",
            "PAB",
            "PEN",
            "PGK",
            "PHP",
            "PKR",
            "PLN",
            "PYG",
            "QAR",
            "RON",
            "RSD",
            "RUB",
            "RWF",
            "SAR",
            "SBD",
            "SCR",
            "SDG",
            "SEK",
            "SGD",
            "SHP",
            "SLL",
            "SOS",
            "SRD",
            "SSP",
            "STD",
            "SVC",
            "SYP",
            "SZL",
            "THB",
            "TJS",
            "TMT",
            "TND",
            "TOP",
            "TRY",
            "TTD",
            "TWD",
            "TZS",
            "UAH",
            "UGX",
            "USD",
            "UYU",
            "UZS",
            "VEF",
            "VES",
            "VND",
            "VUV",
            "WST",
            "XAF",
            "XAG",
            "XAU",
            "XCD",
            "XDR",
            "XOF",
            "XPD",
            "XPF",
            "XPT",
            "YER",
            "ZAR",
            "ZMW",
            "ZWL",
        ]

# Create SQLAlchemy engine and session
engine = create_engine('sqlite:///currency_converter.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

# Create a base class for SQLAlchemy models
Base = declarative_base()

# Define CurrencyPair model
class CurrencyPair(Base):
    __tablename__ = 'currency_pairs'

    id = Column(Integer, primary_key=True)
    base_currency = Column(String)
    quote_currency = Column(String)
    exchange_rate = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)

# Create database tables
Base.metadata.create_all(engine)

# Create a currency converter object
converter = CurrencyRates()

# Define a function to convert currency
def convert_currency(amount, from_currency, to_currency):
    try:
        rate = converter.get_rate(from_currency, to_currency)
        converted_amount = round(amount * rate, 2)
        return converted_amount
    except Exception as e:
        st.write(f"<h3>Error: {e}</h3>", unsafe_allow_html=True)
        return None

# Define the Streamlit app
def app():
    st.title("Currency Converter")
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://cutewallpaper.org/28/clean-dark-wallpaper-hd/1333232585.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

    # Input amount and currencies to convert
    amount = st.number_input("Enter the amount to convert:")
    from_currency = st.selectbox("From currency:", instrument_array)  # Add more currencies as needed
    to_currency = st.selectbox("To currency:", instrument_array)  # Add more currencies as needed

    # Convert currency and display result
    if st.button("Convert"):
        result = convert_currency(amount, from_currency, to_currency)
        if result is not None:
            st.write(
                f"<h3>{amount} {from_currency} = {result} {to_currency}</h3>",
                unsafe_allow_html=True,
            )

            # Save converted currency pair to database
            currency_pair = CurrencyPair(
                base_currency=from_currency,
                quote_currency=to_currency,
                exchange_rate=result,
                timestamp=datetime.utcnow()
            )
            session.add(currency_pair)
            session.commit()


# Run the app
if __name__ == "__main__":
    app()
