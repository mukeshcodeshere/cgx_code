# app/routes.py
from flask import Blueprint, render_template, request, redirect, url_for
from .models import CurrencyPair, db

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    currency_pairs = CurrencyPair.query.all()
    return render_template('index.html', currency_pairs=currency_pairs)

@bp.route('/trade', methods=['GET', 'POST'])
def trade():
    if request.method == 'POST':
        base_currency = request.form['base_currency']
        quote_currency = request.form['quote_currency']
        quantity = float(request.form['quantity'])

        # Perform trading logic here
        # For simplicity, let's just redirect back to the trade page after submission
        return redirect(url_for('main.trade'))

    return render_template('trade.html')
