from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h2>Xin chào từ Flask trên Render!</h2>"
