from webapp import app, db
from flask import request

from ..models.user_model import User

@app.route('/newuser', methods=['POST'])
def newuser():
    """
    Adds a new user to the database
    """
    data = request.get_json()

    username = data['username']
    email = data['email']
    password_hash = data['password_hash']

    user = User(username=username, email=email, password_hash=password_hash)

    db.session.add(user)
    db.session.commit()
    return "Gotcha"
