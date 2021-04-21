from flask import Flask
app = Flask(__name__)  #so flask knows where to look for templates and static files

@app.route('/')  #decorators add functionality to existing functions
@app.route('/home') 
def home():
    return '<h1>Home Page</h1>'

@app.route('/about')  
def about():
    return '<h1>About us</h1>'

if __name__ == "__main__":
    app.run(debug=True)
#need to set environment variable to file that we want to be the flask application
