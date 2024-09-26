"""Seed file to make sample data for users db."""

from models import User, Post, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
User.query.delete()

# Add Users
aaron = User(first_name='Aaron', last_name='Smith', image_url='https://www.freeiconspng.com/thumbs/profile-icon-png/profile-icon-9.png')
maximus = User(first_name='Maximus', last_name='Davis', image_url='https://www.freeiconspng.com/thumbs/profile-icon-png/profile-icon-9.png')
david = User(first_name='David', last_name='Edison', image_url='https://www.freeiconspng.com/thumbs/profile-icon-png/profile-icon-9.png')

# Add new objects to session, so they'll persist
db.session.add(aaron)
db.session.add(maximus)
db.session.add(david)

# Commit--otherwise, this never gets saved!
db.session.commit()

# Add posts
post1 = Post(title='First Post', content='This is my first post.', user_id=1)
post2 = Post(title='Second Post', content='This is my second post.', user_id=2)
post3 = Post(title='Third Post', content='This is my third post.', user_id=3)

# Add new objects to session, so they'll persist
db.session.add_all([post1, post2, post3])
db.session.commit()