import os

from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask import render_template
from flaskext.markdown import Markdown

app = Flask(__name__)
Bootstrap(app)
Markdown(app)

VERSION=0.1

@app.route("/")
def hello():
    welcome_path = "{}/markdown/welcome.md".format(os.path.dirname(__file__))
    with open(welcome_path, 'r') as cf:
            welcome = cf.read()
    return render_template('welcome.html', welcome=welcome, version=VERSION)

if __name__ == "__main__":
    app.run(debug=True)
