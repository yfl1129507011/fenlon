from app import app
from ..model.UserModel import User, db
from flask_login import login_required

@app.route('/')
def index():
    # u = User(username='admin', password='111111')
    # u = User()
    # u.email = 'yfl@fenlon.com'
    # u.mobile = '123456'
    # db.session.add(u)
    # db.session.commit()
    # db.drop_all()
    # db.create_all()
    return 'index'


@app.route('/secret')
@login_required
def secret():
    return 'sign in'