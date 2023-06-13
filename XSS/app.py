from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        content = request.form['content']
        if 'p1' in content or 'p2' in content or 'p3' in content:
            return content + ' Adopted!'
        else:
            return 'Not a valid snake'
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)