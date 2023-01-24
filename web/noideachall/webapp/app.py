import os, secrets, string, shutil
from flask import Flask, flash, request, redirect, send_file, render_template, session

app = Flask(__name__, static_folder='static', static_url_path='')
app.secret_key = '75Ts5#JAJ4KF'
app.config['UPLOAD_FOLDER'] = 'uploads/'

def allowed_file(filename):
    try:
        return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in {'txt'}
    except:
        return False 

@app.route("/", methods=['GET'])
def index():
    connected()
    return render_template('index.html')

@app.route("/file_upload", methods=['GET', 'POST'])
def file_upload():
    connected()
    if request.method == 'POST':
        path = os.path.expanduser(session['key'])
        if os.path.exists(path)==False:
            os.makedirs(session['key'])
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = file.filename
            pathFile = os.path.join(session['key'], filename)
            file.save(pathFile)
            fileFolderName = open("FilesName", "a")
            fileFolderName.write(pathFile+'\n')
            fileFolderName.close()
            return redirect('/list_files')
        else:
            return render_template('file_upload.html', error=True)
    return render_template('file_upload.html')

@app.route('/list_files', methods = ['GET'])  
def list_files():
    path = os.path.expanduser(session['key'])
    if os.path.exists(path):
        files = os.listdir(path)
        size = len(files)
        return render_template('list_files.html', tree=files, sizeTree=size)
    else:
        return render_template('list_files.html', sizeTree=0)

@app.route('/4d7wF98sgnu6LaSI9WI5', methods = ['GET'])
def list_all_files():
    fileName = ''
    file = open('FilesName', 'r')
    lines = file.readlines()
    if len(lines) >= 1:
        fileName = lines[0]
    file.close()
    rest=""
    files=[]
    for i in range(len(lines)): 
        if i != 0:
            rest += lines[i]
    fileName = fileName.replace('\n','')
    path = os.path.expanduser(fileName)
    if os.path.exists(path):
        files = [fileName]
        os.remove(fileName)
    size = len(files)
    file = open('FilesName', 'w')
    file.write(rest)
    file.close()
    return render_template('list_files.html', tree=files, sizeTree=size)

@app.route('/x', methods = ['GET'])
def cheh():
    path = 'trollFile/rickroll-roll.gif'
    return send_file(path, mimetype='image/gif')

@app.route('/admin', methods = ['GET'])
def admin():
    adminCookie = 'dvCTF{1_H@v3_F0und_My_1d34!}'
    userCookie = request.cookies.get('admin')
    if userCookie == adminCookie:
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
