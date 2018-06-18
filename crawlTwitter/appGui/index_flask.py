from flask import Flask, render_template, request, flash
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '../'
ALLOWED_EXT = {'.txt'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/index')
def upload_file():
    return render_template('index.html')


@app.route('/uploading', methods=['GET', 'POST'])
def upload_file1():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        return render_template('uploading.html')


if __name__ == '__main__':
    app.run(debug=True)
