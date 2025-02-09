from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = 'Users'
    
    UserID = db.Column(db.Integer, primary_key=True)
    Username = db.Column(db.String(100), unique=True, nullable=False)
    PasswordHash = db.Column(db.String(200), nullable=False)
    CreatedAt = db.Column(db.DateTime)

    def __init__(self, username, password):
        self.Username = username
        self.PasswordHash = generate_password_hash(password)  # Băm mật khẩu khi tạo user

    def check_password(self, password):
        return check_password_hash(self.PasswordHash, password)  # Kiểm tra mật khẩu khi login

    def get_id(self):
        return str(self.UserID)  # Override get_id to return UserID
