from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)  #so flask knows where to look for templates and static files

app.config['SECRET_KEY'] ='fdc03f61e31fac890e1e89617fabac1e'  #make an environment variable later
# (in terminal)
# import secrets
# secrets.token_hex(16)  16 is the number of bytes

posts = [{"title":"first post", "author": "bob", "content": "my first post", "date_posted":"Apr 22, 2021"},
{"title":"second post", "author": "david", "content": "my second post", "date_posted":"Apr 23, 2021"}]


@app.route('/')  #decorators add functionality to existing functions
@app.route('/home') 
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')  
def about():
    return render_template('about.html', title="About")

@app.route('/register', methods=['GET', 'POST'])  
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # the 'success' string refers to the bootstrap class
        flash(f'Account created for {form.username.data}!', category='success')
        return redirect(url_for('home'))
    return render_template('register.html', title="Register", form=form)

@app.route('/login', methods=['GET', 'POST'])  
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been successfully logged in!', category='success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check username and password', category='danger')
    return render_template('login.html', title="Login", form=form)

if __name__ == "__main__":
    app.run(debug=True)
#need to set environment variable to file that we want to be the flask application
