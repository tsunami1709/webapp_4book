
from flask import Flask, render_template, request, redirect, url_for, session

from mongodb import get_all_signup

    
app = Flask(__name__)
# app.secret_key='abcss3d567a17ddd289'

@app.route('/')
def index():
    # if 'username' in session:
    #     return 'You are logged in as ' + session['username']
    return render_template('index.html')

@app.route('/login', methods=['GET'])
def get_login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def post_login():
    username_login= request.form.get("usernames")
    password_login= request.form.get("passwords")
    for v in get_all_signup():
        if v['username'] == username_login and v['password']== password_login:       
             # session ['username'] = username_ss
            return render_template('index.html')
    return 'user/pass sai'
    # return password_login

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)