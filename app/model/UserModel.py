from .. import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(UserMixin, db.Model):
    __tablename__ = 'fl_user'

    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    username = db.Column(db.VARCHAR(16), nullable=False, server_default='', unique=True)
    password_hash = db.Column(db.CHAR(128), nullable=False, server_default='')
    # email = db.Column(db.String(32), nullable=False, server_default='')
    # mobile = db.Column(db.String(32), nullable=False, server_default='')
    login_num = db.Column(db.INT, nullable=False, server_default='0')
    reg_time = db.Column(db.Integer, nullable=False, server_default='0')
    reg_ip = db.Column(db.BigInteger, nullable=False, server_default='0')
    last_login_time = db.Column(db.Integer, nullable=False, server_default='0')
    last_login_ip = db.Column(db.BigInteger, nullable=False, server_default='0')
    update_time = db.Column(db.DateTime, nullable=False, server_default=func.now())
    status = db.Column(db.SmallInteger, nullable=False, server_default='0')

    def __repr__(self):
        return '<User %r>' % self.username

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, pwd):
        from werkzeug.security import generate_password_hash
        self.password_hash = generate_password_hash(pwd)

    def checkPwd(self, pwd):
        from werkzeug.security import check_password_hash
        return check_password_hash(self.password_hash, pwd)