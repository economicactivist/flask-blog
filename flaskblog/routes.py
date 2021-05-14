from flask import render_template, url_for, flash, redirect
from flaskblog import app
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post

@ app.route('/')  # decorators add functionality to existing functions
@ app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@ app.route('/about')
def about():
    return render_template('about.html', title="About")


@ app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # the 'success' string refers to the bootstrap class
        flash(f'Account created for {form.username.data}!', category='success')
        return redirect(url_for('home'))
    return render_template('register.html', title="Register", form=form)


@ app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@email.com' and form.password.data == 'password':
            flash('You have been successfully logged in!', category='success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check username and password',
                  category='danger')
    return render_template('login.html', title="Login", form=form)
