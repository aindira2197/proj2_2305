from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))


@app.route('/')
def home():

    users = User.query.all()

    text = ""

    for user in users:
        text += f"{user.id} - {user.name}<br>"

    return text


@app.route('/add/<name>')
def add_user(name):

    user = User(name=name)

    db.session.add(user)
    db.session.commit()

    return f"{name} added!"


if __name__ == '__main__':

    with app.app_context():
        db.create_all()

    app.run(debug=True)
