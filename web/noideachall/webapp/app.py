import os
from flask import Flask, flash, request, redirect, send_file, render_template

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
    return render_template('index.html')

@app.route("/file_upload", methods=['GET', 'POST'])
def file_upload():
    if request.method == 'POST':
        path = os.path.expanduser(u'uploads')
        if os.path.exists(path)==False:
            os.makedirs('uploads')
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
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect('/list_files')
        else:
            return render_template('file_upload.html', error=True)
    return render_template('file_upload.html')

@app.route('/list_files', methods = ['GET'])  
def list_files():
    path = os.path.expanduser(u'uploads')
    if os.path.exists(path):
        files = os.listdir(path)
        size = len(files)
        return render_template('list_files.html', tree=files, sizeTree=size)
    else:
        return render_template('list_files.html', sizeTree=0)

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

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)