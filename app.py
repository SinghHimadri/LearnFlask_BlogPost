from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///posts.db'
db= SQLAlchemy(app)

class BlogPost(db.Model):
    id=

all_posts= [
    {
        'title' : 'Post 1',
        'content' : 'This is the content post 1',
        'author' : 'Timtim' 
    },
    {
        'title': 'Post 2',
        'content': 'This is the content post 2'
    }
]

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/posts')
def posts():
    return render_template('posts.html',posts = all_posts)


if __name__ == "__main__":
    app.run(debug=True)   