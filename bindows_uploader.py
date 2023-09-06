import os
from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)
UPLOAD_FOLDER = '/tmp'

# Configure the upload folder
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file:
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)
        return 'File uploaded successfully!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5055, debug=True)
