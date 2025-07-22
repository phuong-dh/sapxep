from flask import Flask, render_template, request, send_file
import os
import openpyxl
# import các thư viện và copy lại toàn bộ hàm process từ ok.py vào đây (bạn chỉ cần bỏ code giao diện tkinter)

app = Flask(__name__)

# ----- COPY HÀM process() và các hàm phụ trợ vào đây -----
def process(input_file, input_sheet):
    # ... (copy y nguyên hàm process trong ok.py vào đây) ...
    # Nhớ sửa lại để không dùng filedialog/messagebox, chỉ return hoặc raise Exception khi lỗi.
    pass

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["file"]
        sheet_name = request.form.get("sheet")
        if not file or not sheet_name:
            return "Vui lòng chọn file và sheet!", 400
        file.save("input.xlsx")
        try:
            process("input.xlsx", sheet_name)
            return send_file("ket_qua.xlsx", as_attachment=True)
        except Exception as e:
            return f"Lỗi: {e}", 500
    else:
        # Nếu GET, trả về form HTML upload file
        return '''
        <h2>Upload file Excel SORT xe Bình Anh</h2>
        <form method="post" enctype="multipart/form-data">
            File: <input type="file" name="file" accept=".xlsx" required><br>
            Tên Sheet: <input type="text" name="sheet" value="Sheet1" required><br>
            <button type="submit">Chạy SORT</button>
        </form>
        '''

if __name__ == "__main__":
    app.run(debug=True)
