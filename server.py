from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from config import DevConfig 

app = Flask(__name__)
app.config.from_object(DevConfig)
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(120))
    password_hash = db.Column(db.String(255))


    def __str__(self):
        return "<User: {}>".format(self.username)

@app.route('/')
def index():
    return "<h1>Hello Flask</h1>"


@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db, User=User)

