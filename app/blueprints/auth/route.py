from flask import redirect, render_template, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from app import login
from flask_login import current_user, login_user, logout_user
from app.blueprints.auth import auth
from app.blueprints.auth.form import LoginForm, RegisterForm, UserEditForm
from app.blueprints.auth.model import User, is_user_unique
from app import db
import re

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

@auth.route('/login', methods=['POST', 'GET'])
def login():
	login_form = LoginForm()
	if current_user.is_anonymous:
		if request.method == "POST":
			if login_form.validate_on_submit():
				user = User.query.filter_by(username=login_form.username.data).first()
				if user and check_password_hash(user.password, login_form.password.data):
					login_user(user)
					return redirect(url_for('tasks.tasksList'))
				else:
					flash('Login typed incorrectly or user does not exist.')
	else:
		return redirect(url_for('tasks.tasksList'))

	return render_template('auth/login.html', login_form=login_form)

@auth.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('auth.login'))

@auth.route('/register', methods=['POST', 'GET'])
def register():
	register_form = RegisterForm()
	if request.method == 'POST':
		regex = r"^(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]+$"
		username_check = is_user_unique(register_form.username.data)
		if username_check:
			if re.match(regex, register_form.password.data) and re.match(regex, register_form.confirm_password.data):
				if register_form.password.data != register_form.confirm_password.data:
					flash('Passwords must match!')
				else:
					user = User(username=register_form.username.data, password=generate_password_hash(register_form.password.data))
					db.session.add(user)
					db.session.commit()
					return redirect(url_for('auth.login'))
			else:
				flash('Passwords must contain 1 alphabetical and 1 numeric')
		else:
			flash('Username already exists')
	return render_template('auth/register.html', register_form=register_form)

@auth.route('/userEdit', methods=['POST', 'GET'])
def userEdit():
	user_edit_form = UserEditForm()
	user_stmt = User.query.filter_by(id=current_user.id).first()
	if user_edit_form.validate_on_submit():
		user_stmt.username = user_edit_form.username.data
		db.session.commit()
		return redirect(url_for('tasks.tasksList'))
	user_edit_form.username.data = user_stmt.username
	return render_template('/auth/userEdit.html', user_edit_form=user_edit_form)

