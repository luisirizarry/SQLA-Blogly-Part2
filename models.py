"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class User(db.Model):
    """User."""
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    image_url = db.Column(db.String, nullable=False, default='https://www.freeiconspng.com/thumbs/profile-icon-png/profile-icon-9.png')
    
    @classmethod
    def get_all_users(cls):
        """Return all users."""
        return cls.query.all()

    def __repr__(self):
        """Show info about user."""
        fullName = self.get_full_name()
        return f"<User {fullName}>"
    
    def get_full_name(self):
            """Return full name of user."""
            return f"{self.first_name} {self.last_name}"
    
    