from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
import os
import json

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))

try:
    with open(os.path.join(SITE_ROOT, 'config.local.json')) as f:
        JSON_DATA = json.load(f)
except FileNotFoundError:
    with open(os.path.join(SITE_ROOT, 'config.json')) as f:
        JSON_DATA = json.load(f)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://' + JSON_DATA['db_user'] + ':'\
                                        + JSON_DATA['db_pass'] + '@localhost/' + JSON_DATA['db_name']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=os.environ.get('DEBUG', False))

