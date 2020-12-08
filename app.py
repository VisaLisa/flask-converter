from flask import Flask, render_template, redirect, request, session, flash
from flask_debugtoolbar import DebugToolbarExtension
from forex_python.converter import CurrencyRates, CurrencyCodes

app = Flask(__name__)
# the toolbar is only enabled in debug mode:
app.debug = True
# set a 'SECRET_KEY' to enable the Flask session cookies
app.config['SECRET_KEY'] = 'St0NKs&M0N13z'
toolbar = DebugToolbarExtension(app)

c = CurrencyRates()
s = CurrencyCodes()

@app.route("/", methods=['GET','POST'])
def home():
    return render_template('base.html')

"""Currency Check"""
@app.route("/currency-check", methods=["POST"])
def currency_check():
    c_from = request.form.get['c-from'].upper()
    c_to = request.form.get['c-to'].upper()
    amount = request.form.get['amount']
    print (amount)
    
    # try:
    #     c.get_rates(c_from)
    #     c_from = c_from
    # except:
    #     flash('The currency you were converting from was invalid')
    #     c_from = False 
    # try:
    #     c.get_rates(c_to)
    #     c_to = c_to
    # except:
    #     flash('The currency you were converting to was invalid')
    #     c_to = False
    # if c_from and c_to and amount.replace('.', '', 1).isdigit():
    #     amount = str(round(c.convert(c_from, c_to, float(amount)),2)) 
    #     symbol = s.get_symbol(c_to)
    # elif not amount.isnumeric():
    #     flash('The amount you put in was invalid')
    #     symbol = False
    #     amount=False
    # else:
    #     symbol = False
    #     amount = False

    return render_template('base.html', amount=amount, c_from=c_from, c_to=c_to)
