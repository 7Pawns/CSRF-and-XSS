from flask import Flask, render_template, url_for, request, make_response
from flask_api import status

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():

    return render_template('index.html')

@app.route("/setcookie", methods=['POST'])
def setcookie():
    if request.method == 'POST':
        content = request.form['name']
        resp = make_response('Done!') 
        resp.set_cookie('name', content)
        return resp

@app.route("/api", methods=['POST'])
def changePrice():
    if request.cookies.get('name') != 'admin':
        return '403 Forbidden', status.HTTP_403_FORBIDDEN
    
    return render_template('index.html', id=request.form['id'], price=request.form['price'])

if __name__ == "__main__":
    app.run(debug=True)