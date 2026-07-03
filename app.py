from flask import Flask, jsonify

app = Flask(__name__)

# Trang chính
@app.route("/")
def home():
    return "Hoàng Hiệp Gaming Server đang chạy 🔥"

# API game giả lập
@app.route("/api/player")
def player():
    return jsonify({
        "name": "HoangHiep",
        "level": 10,
        "coin": 9999
    })

# chạy server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)