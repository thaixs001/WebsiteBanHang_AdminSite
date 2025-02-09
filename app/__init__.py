from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os
from dotenv import load_dotenv

# Tải các biến môi trường từ .env file
load_dotenv()

# Khởi tạo Flask app
app = Flask(__name__)

# Cấu hình cho Flask
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'defaultsecretkey')  # Mã hóa phiên làm việc
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'mssql+pyodbc://sa:1234aa@localhost/BanHangOnline?driver=ODBC+Driver+17+for+SQL+Server')  # Cấu hình CSDL SQL Server
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Tắt theo dõi thay đổi không cần thiết

# Khởi tạo các extension
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'  # Đảm bảo route 'login' có thể truy cập khi chưa đăng nhập

# Import User model
from app.models.user import User

# Định nghĩa hàm user_loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))  # Tìm người dùng theo ID trong CSDL

# Import các controller sau khi app đã được khởi tạo
from app.controllers import auth_controller, post_controller, main_controller
