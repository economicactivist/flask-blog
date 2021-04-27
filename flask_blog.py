from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
from datetime import datetime

# so flask knows where to look for templates and static files
app = Flask(__name__)

# make an environment variable later
app.config['SECRET_KEY'] = 'fdc03f61e31fac890e1e89617fabac1e'
# /// means relative path from current file (i.o.w, same directory)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)  # database instance
# (in terminal)
# import secrets
# secrets.token_hex(16)  16 is the number of bytes


class User(db.Model):
    # implicit __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False,
                           default="default.jpg")
    # unique not true because there needs to be a default profile picture
    password = db.Column(db.String(60), nullable=False)
    # password will be hashed to a 60-character string
    # unique not true because two different users can have the same password
    posts = db.relationship('Post', backref="author", lazy=True)
    # lazy=True is like a normal select statement
    # backref is a shortcut that prevents having to place an explict back_populates
    # on both models/tables.  However, this is confusing because the other table doesn't
    # have an author field.  Schafer says it's like creating a new column in the Post model

    def __repr__(self):
        return f'User("{self.username}", "{self.email}", "{self.image_file}")'


class Post(db.Model):
    # implicit __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)
    # dont use datetime.utcnow() because you want to pass
    # in the function, not the current time, as the argument
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'Post("{self.title}", "{self.date_posted}")'


posts = [{"title": "first post", "author": "bob", "content": "my first post", "date_posted": "Apr 22, 2021"},
         {"title": "second post", "author": "david", "content": "my second post", "date_posted": "Apr 23, 2021"}]


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


if __name__ == "__main__":
    app.run(debug=True)
# need to set environment variable to file that we want to be the flask application
