from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import URL
import os

url = URL.create(
    drivername="postgresql",
    username="naturenotice",
    host=os.environ.get("DB_HOST"),
    database="db_nature_notice",
    password=os.environ.get("DB_PASSWORD")
)

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

@app.route('/')
def hello():
    return 'My First API !!'
