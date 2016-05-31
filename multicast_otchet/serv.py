from flask import render_template
from flask import Flask
app = Flask(__name__)
import os
@app.route("/")
def hello():
    return render_template('index.html')

@app.route('/test')
def test():
    print os.getcwd()
    return render_template('test.html')

@app.route('/new')
def new():
    return render_template('new.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
