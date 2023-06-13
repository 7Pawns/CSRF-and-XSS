from flask import Flask, render_template, url_for, request, make_response, abort, session
from flask_api import status
from uuid import uuid4

app = Flask(__name__)
app.secret_key = uuid4().hex

# Inital Pizzas Prices
prices = {'p1' : '100$', 'p2' : '150$', 'p3' : '200$'}

# Main page
@app.route("/", methods=['GET', 'POST'])
def index():
    session['anti_csrf_token'] = uuid4().hex
    print(session)
    return render_template('index.html', prices=prices, anticsrf=session['anti_csrf_token'])

# Simple cookie setter (just name)
@app.route("/setcookie", methods=['POST'])
def setcookie():
    if request.method == 'POST':
        content = request.form['name']
        resp = make_response('Done!') 
        resp.set_cookie('name', content)
        return resp

# API for changing prices that will be attacked using CSRF
@app.route("/api", methods=['POST'])
def changePrice():
    if 'anti_csrf_token' not in request.form:
        return abort(400)
    if request.cookies.get('name') != 'admin':
        return abort(403)
    if session['anti_csrf_token'] != request.form['anti_csrf_token']:
        return abort(401)
    id = request.form['id']
    price = request.form['price']
    prices[id] = price + '$'
    return render_template('index.html', prices=prices, anticsrf=session['anti_csrf_token'])

if __name__ == "__main__":
    app.run(debug=True)