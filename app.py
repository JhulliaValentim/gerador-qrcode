from flask import Flask, render_template, request, send_file
import qrcode
from io import BytesIO
app = Flask(__name__)
@app.route('/', methods=['Get','POST'])
def index():
    qr_code_base64=None
    if request.method == 'POST':
        data = request.form.get('data')
        if data:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(data)
            qr.make(fit=True)
            img=qr.make_image(fill_color="black", back_color="white")
            buffer = BytesIO()
            img.save(buffer, format='png')
            buffer.seek(0)
            import base64
            qr_code_base64 = base64.b64encode(buffer.getvalue()).decode()
            return render_template('index.html', qr_code_base64=qr_code_base64)
        return render_template('index.html', qr_code_base64=qr_code_base64)
    return render_template('index.html', qr_code_base64=qr_code_base64)
if __name__ == '__main__':
    app.run(debug=True)
