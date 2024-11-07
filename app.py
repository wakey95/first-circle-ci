from flask import Flask

# Tạo một ứng dụng Flask
app = Flask(__name__)

# Định nghĩa route chính
@app.route('/')
def home():
    return "Hello, World!"

# Chạy ứng dụng Flask
if __name__ == '__main__':
    app.run(debug=True)
