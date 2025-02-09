 
from werkzeug.security import generate_password_hash

# Mật khẩu gốc
password = "1234aa"

# Băm mật khẩu
hashed_password = generate_password_hash(password)

print(hashed_password)  # In ra mật khẩu đã băm
