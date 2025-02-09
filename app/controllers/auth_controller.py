from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, current_user, logout_user
from werkzeug.security import check_password_hash
from app import app
from app.models.user import User

@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home_page'))  # Chuyển đến trang chính nếu đã đăng nhập

    if request.method == "POST":
        username = request.form['username']
        password = request.form['current-password']

        # Tìm user theo Username (chữ "U" viết hoa)
        user = User.query.filter_by(Username=username).first()
        
        if user:
            print(f"Đã tìm thấy người dùng: {user.Username}")  # Debug: Kiểm tra xem có tìm thấy user không
            print(f"Hash được lưu trữ: {user.PasswordHash}")  # Debug: In mật khẩu đã băm từ CSDL

            # Kiểm tra mật khẩu
            if check_password_hash(user.PasswordHash, password):
                print("Mật khẩu khớp.")  # Debug: Mật khẩu khớp
                login_user(user)
                flash("Đăng nhập thành công!", 'success')
                return redirect(url_for("home_page"))  # Chuyển đến trang chính
            else:
                print("Mật khẩu không khớp.")  # Debug: Mật khẩu không khớp
                flash("Sai tên đăng nhập hoặc mật khẩu", 'danger')
        else:
            print("Không tìm thấy người dùng.")  # Debug: Nếu không tìm thấy user
            flash("Sai tên đăng nhập hoặc mật khẩu", 'danger')

    return render_template('index.html')  # Trả về trang đăng nhập

@app.route('/forgot_password')
def forgot_password():
    return render_template('forgot_password.html')

@app.route('/forgot_password_action', methods=['POST'])
def forgot_password_action():
    email = request.form.get('emailInput')
    # Add logic to handle password reset, e.g., send a reset email
    print(f"Password reset requested for email: {email}")  # Debug: In email được nhập
    flash("Nếu email tồn tại trong hệ thống, bạn sẽ nhận được hướng dẫn khôi phục mật khẩu.", 'info')
    return redirect(url_for('index'))  # Redirect back to login page

@app.route('/logout')
def logout():
    logout_user()
    flash("Bạn đã đăng xuất thành công!", 'success')
    return redirect(url_for('login'))  # Chuyển hướng đến trang đăng nhập
