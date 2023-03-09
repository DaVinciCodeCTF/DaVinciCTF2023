import os, secrets, string
from flask import Flask, request, redirect, send_file, render_template, session

app = Flask(__name__, static_folder='static', static_url_path='')
app.secret_key = '75Ts5#JAJ4KF'

UPLOAD_FOLDER = 'uploads/'
FLAG = 'dvCTF{1_H@v3_F0und_My_1d34!}'
FILE_QUEUE = []

def allowed_file(filename):
    return '\\' not in filename and '/' not in filename and '.' in filename and filename.rsplit('.', 1)[1].lower() in ['txt']

@app.route("/", methods=['GET'])
def index():
    connected()
    return render_template('index.html')

@app.route("/file_upload", methods=['GET', 'POST'])
def file_upload():
    connected()
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return render_template('file_upload.html', error="No file part")
        file = request.files['file']
        # If the user does not select a file, the browser submits an empty file without a filename.
        if file.filename == '':
            return render_template('file_upload.html', error="No selected file")
        if not file or not allowed_file(file.filename):
            return render_template('file_upload.html', error="You tried to enter an invalid file !")
        if len(FILE_QUEUE) > 30:
            return render_template('file_upload.html', error="I have already received many proposals, please wait a little bit")
        path = os.path.expanduser(UPLOAD_FOLDER + session['key'])
        if not os.path.exists(path):
            os.makedirs(path)
        path_file = os.path.join(path, file.filename)
        file.save(path_file)
        FILE_QUEUE.append(path_file)
        return redirect('/list_files')

    return render_template('file_upload.html')

@app.route('/list_files', methods = ['GET'])  
def list_files():
    connected()
    files = []
    path = os.path.expanduser(UPLOAD_FOLDER + session['key'])
    if os.path.exists(path):
        files = os.listdir(path)
    return render_template('list_files.html', tree=files)

@app.route('/4d7wF98sgnu6LaSI9WI5', methods = ['GET'])
def list_all_files():
    files = []
    if request.cookies.get('admin') == FLAG and len(FILE_QUEUE) != 0:
        file_name = FILE_QUEUE.pop(0)
        path = os.path.expanduser(file_name)
        if os.path.exists(path):
            files = [file_name]
            os.remove(file_name)
    return render_template('list_files.html', tree=files)

@app.route('/x', methods = ['GET'])
def cheh():
    path = 'trollFile/rickroll-roll.gif'
    return send_file(path, mimetype='image/gif')

@app.route('/admin', methods = ['GET'])
def admin():
    if request.cookies.get('admin') == FLAG:
        return render_template('admin.html')
    else:
        return render_template('notAdmin.html')

def connected():
    if 'key' not in session:
        alphabet = string.ascii_letters + string.digits
        value = ''.join(secrets.choice(alphabet) for i in range(20))
        session['key'] = value
    return True

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
