from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.engine import URL


url = URL.create(
    drivername="postgresql",
    username="jabujabu",
    host="/tmp/postgresql/socket",
    database="password_manager"
)

engine = create_engine(url)

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/test")
def bye_world():
    return "<p>bye  World!</p>"



