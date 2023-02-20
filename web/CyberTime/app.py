from flask import Flask, render_template, session, request
import uuid
import os
import re
from urllib.parse import urlparse
import requests
import base64


HOST = os.environ['HOST']
FLAG = 'DVC{C5rF4r34M4Z1N6_75512fef01c266da9d4911d418a0d3e2}'
APP_NAME = 'CyberTime'
ADMINS = {}  # {username: <boolean>}

app = Flask(__name__, static_folder='static', static_url_path='')
app.secret_key = os.urandom(20)


def is_bot():
    cookie = request.cookies.get('bot', default='')
    return cookie == FLAG


@app.route('/', methods=['GET'])
def home():
    if 'username' not in session:
        session['username'] = 'user-' + str(uuid.uuid4())
    return render_template('home.html', app_name=APP_NAME, username=session['username'])


@app.route('/admin/dashboard', methods=['GET'])
def dashboard():
    if 'username' not in session:
        session['username'] = 'user-' + str(uuid.uuid4())
    is_admin = 'true' if (session['username'] in ADMINS and ADMINS[session['username']] or is_bot()) else 'false'
    return render_template('dashboard.html', app_name=APP_NAME, username=session['username'], is_admin=is_admin)


@app.route('/admin/dashboard/add', methods=['GET'])
def add_admin():
    if ('username' in session and session['username'] in ADMINS and ADMINS[session['username']]) or is_bot():
        username = request.args.get('username', default='')
        if username != '':
            ADMINS[username] = True
            return username + ' is now an admin'
        else:
            return 'Please provide a username'
    else:
        return 'Access denied'


@app.route('/feedback', methods=['POST'])
def feedback():
    if 'username' not in session:
        return 'Access denied'
    else:
        try:
            user_feedback = base64.b64decode(request.form['message']).decode(encoding='ISO-8859-1')
            match = re.search(
                r'https?://(www\.)?[-a-zA-Z0-9@:%._+~#=]{1,256}.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_+.~#?&/=]*)',
                user_feedback)
            if match is not None:
                parsed_uri = urlparse(str(match.group(0)))
                if parsed_uri.hostname == HOST:
                    requests.get(str(match.group(0)), cookies={'bot': FLAG})
                else:
                    return 'Why are you sending me this link ?'
            return 'Your feedback is interesting'
        except Exception as e:
            return 'An error occurred while reading your message'


@app.route('/flag', methods=['GET'])
def flag():
    f = FLAG if ('username' in session and session['username'] in ADMINS and ADMINS[session['username']] or is_bot())\
        else 'Access denied'
    return render_template('flag.html', app_name=APP_NAME, flag=f)


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
