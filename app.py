from flask import Flask, render_template_string

app = Flask(__name__)

HTML = '''
<!doctype html>
<html>
<head>
    <title>Đang bảo trì</title>
    <style>
        body {
            background: #f8f8f8;
            font-family: Arial, sans-serif;
            text-align: center;
            margin-top: 100px;
        }
        .container {
            display: inline-block;
            padding: 40px 30px;
            border: 2px solid #1e90ff;
            background: #fff;
            border-radius: 16px;
            box-shadow: 0 4px 20px #0002;
        }
        .maintain {
            color: #e67e22;
            font-size: 2rem;
            font-weight: bold;
            margin-bottom: 20px;
        }
        .contact-btn {
            padding: 12px 28px;
            font-size: 1.1rem;
            background: #1877f2;
            color: #fff;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            text-decoration: none;
            font-weight: bold;
            transition: background 0.2s;
            box-shadow: 0 2px 10px #0001;
        }
        .contact-btn:hover {
            background: #1456a3;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="maintain">🚧 Trang web đang bảo trì! 🚧</div>
        <p>Liên hệ admin để biết thêm chi tiết hoặc nhận hỗ trợ.</p>
        <a class="contact-btn" href="https://www.facebook.com/oanhuynhphuong.651928/" target="_blank">
            Liên hệ Facebook Phương ĐH
        </a>
    </div>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(HTML)

if __name__ == '__main__':
    app.run()
