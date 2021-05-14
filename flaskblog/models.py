from flaskblog import db
from datetime import datetime

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
    # 'Post' is capitalized because the Post class is being referenced
    # lazy=True is like a normal select statement that grabs the whole table at once
    # backref is a shortcut that prevents having to place an explict back_populates
    # on both models/tables.  However, this is confusing because the other table doesn't
    # have an author field.  Schafer says it's like creating a new column in the Post model
    # posts is not a column but rather an attribute of the class.  it runs a query on a specific
    # instance of the User class and returns a list of post instances associated with that instance
    # (every instance will be associated with a specific user_id)

    """ ***Example***
        user_1 = User(username="David", email="david@yahoo.com", password="password")
        user_2 = User(...)
        db.session.add(user_1)
        db.session.commit()
        [other commands: User.query.all(); User.query.first(); User.query.filter_by()]
        user = User.query.filter_by(username="Corey").first()  #use first() so that it's not a list
        #could also say "user = User.query.get(1)
        [now you can do things on the instance like "user.id"]
        ***to the point***
        now you can say "user.posts" to run a query on User('David', 'david@yahoo.com', 'default.jpg')
        1) user.posts returns an empty list
        2) post_1 = Post(title="First post", content="My First Post", user_id=user.id) #note user.id not user_id
           post_2 = Post(title="Second post", content="My Second Post", user_id=user.id)
        3) db.session.add(post_1)
           db.session.add(post_2)
           db.session.commit()
        4) user.posts returns [Post('First Post', '2021-xx-xx ....'), Post('Second Post', '2021-xx-xx ....')]
        5) post = Post.query.first()
        6) post.user_id   returns 1
        ***important***
        7) post.author returns User('David', 'david@yahoo.com', 'default.jpg')
        so using backref="author" allows a post instance to hook into the associated user instance 
        and return it. (You can also think of it as creating an invisible extra column in the posts table 
        that holds the user instance)
        
    """

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
    # 'user.id' is lowercase because it is referencing the table name and
    # column name (not the User class)

    def __repr__(self):
        return f'Post("{self.title}", "{self.date_posted}")'


posts = [{"title": "first post", "author": "bob", "content": "my first post", "date_posted": "Apr 22, 2021"},
         {"title": "second post", "author": "david", "content": "my second post", "date_posted": "Apr 23, 2021"}]