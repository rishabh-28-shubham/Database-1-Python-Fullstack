from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from config import Config
from models import db, User, Post
import uuid
from datetime import date

app = Flask(__name__)
app.config.from_object(Config)

# Initialize SQLAlchemy with the app
db.init_app(app)

# Create database tables before first request
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def index():
    # Query all posts with their authors
    posts = Post.query.join(User).all()
    return render_template('index.html', posts=posts)

@app.route('/add-post', methods=['GET', 'POST'])
def add_post():
    if request.method == 'POST':
        # Get form data
        title = request.form['title']
        content = request.form['content']
        # Hardcoded user_id for simplicity; in production, use authenticated user
        user_id = 'aec92dd8-79dd-4b22-9deb-a2af00d568c8'
        
        # Create new post
        new_post = Post(
            id=str(uuid.uuid4()),
            user_id=user_id,
            title=title,
            content=content,
            created_at=date.today()
        )
        
        # Add and commit to database
        db.session.add(new_post)
        db.session.commit()
        
        return redirect(url_for('index'))
    
    return render_template('add_post.html')

@app.route('/add-user')
def add_user():
    # Check if user exists to avoid duplicate key error
    if not User.query.filter_by(username='rishabh').first():
        new_user = User(
            id=str(uuid.uuid4()),
            username='rishabh',
            email='rishabh@example.com'
        )
        db.session.add(new_user)
        db.session.commit()
        return f'User {new_user.username} added.'
    return 'User already exists.'

if __name__ == '__main__':
    app.run(debug=True)