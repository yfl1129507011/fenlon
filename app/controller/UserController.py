from app import app, lm
from flask import render_template, redirect, request, url_for
from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Required, Length
from flask_login import login_user, logout_user, current_user
import json
from ..model.UserModel import User, db

class LoginForm(Form):
    username = StringField('账号', validators=[Required(), Length(1, 64)])
    password = PasswordField('密码', validators=[Required(), Length(6)])
    submit = SubmitField('登录')

class registerForm(Form):
    username = StringField('账&emsp;&emsp;号', validators=[Required(), Length(1, 64)])
    password = PasswordField('密&emsp;&emsp;码', validators=[Required(), Length(6)])
    repassword = PasswordField('确认密码', validators=[Required(), Length(6)])
    submit = SubmitField('免费注册')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        data = {'status': 404}
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
            if user is not None and user.checkPwd(form.password.data):
                login_user(user)
                data['status'] = 200
                data['url'] = (request.args.get('next') or url_for('index'))
            else:
                data['info'] = '账号或密码错误'
        else:
            data['info'] = '账号或密码格式错误'

        return json.dumps(data)
    else:
        if current_user.is_authenticated == True:
            return redirect(url_for('index'))
        return render_template('home/user/login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = registerForm()
    if request.method == 'POST':
        data = {'status': 404}
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
            if user is not None:
                data['info'] = '该用户已注册'
            else:
                if form.password.data == form.repassword.data:
                    u = User(username=form.username.data, password=form.password.data)
                    db.session.add(u)
                    db.session.commit()
                    login_user(u)
                    data['url'] = (request.args.get('next') or url_for('index'))
                    data['info'] = '注册成功'
                    data['status'] = 200
                else:
                    data['info'] = '密码不一致'
        else:
            data['info'] = '账号或密码格式错误'

        return json.dumps(data)
    else:
        if current_user.is_authenticated == True:
            return redirect(url_for('index'))
        return render_template('home/user/register.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@lm.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))