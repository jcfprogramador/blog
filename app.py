''' comandos abaixo para usar Flask em modo debug = True

usar esses 3 comandos caso use linux ou mac
export FLASK_APP=app
export FLASK_ENV=development
flask run

usar esse comando caso use prompt no windows
set FLASK_ENV=development

usar esse comando caso use shell/terminal no windows
$env:FLASK_ENV = "development"

caso queira rodar em modo debug = True via script (python - m app.py) usar no programa, codigo abaixo:
app.run(debug=True)
if __name__ == '__main__':
    app.run(debug=True)

'''
from flask import Flask, render_template, redirect, url_for
from flask_login import LoginManager, UserMixin
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask("hello")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "jcfranco"

db = SQLAlchemy(app)
login = LoginManager(app)

class Post(UserMixin, db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(70), nullable=False)
    body = db.Column(db.String(500))
    created = db.Column(db.DateTime, nullable=False, default=datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), nullable=False, unique=True, index=True) 
    email = db.Column(db.String(64), nullable=False, unique=True)
    password_hash = db.Column(db.String(128), nullable=False)
    posts = db.relationship('Post', backref='author')


@login.user_loader
def load_user(id):
    return User.query.get(int(id))

db.create_all()

@app.route("/")
def index():
    posts = Post.query.all()
    return render_template("index.html", posts=posts)

def set_password(self, password):
    self.password_hash = generate_password_hash(password)
    
def check_password(self, password):
    return check_password_hash(self.password_hash, password)
