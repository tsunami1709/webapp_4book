import re
import sys
from mongodb import get_all_signup, get_book,sortt
from flask import Flask, render_template, request, redirect, url_for, session
app = Flask(__name__)
app.secret_key='abcss3d567a17ddd289'
import pymongo
from bson.objectid import ObjectId
client = pymongo.MongoClient("mongodb+srv://thangnq:12345678Abc@cluster0-zqxy8.mongodb.net/test?retryWrites=true&w=majority")

db = client.all_book
dbc = client.my_book

patterns = {
    '[àáảãạăắằẵặẳâầấậẫẩ]': 'a',
    '[đ]': 'd',
    '[èéẻẽẹêềếểễệ]': 'e',
    '[ìíỉĩị]': 'i',
    '[òóỏõọôồốổỗộơờớởỡợ]': 'o',
    '[ùúủũụưừứửữự]': 'u',
    '[ỳýỷỹỵ]': 'y'
}


def convert(text):
    output = text
    for regex, replace in patterns.items():
        output = re.sub(regex, replace, output)
        output = re.sub(regex.upper(), replace.upper(), output)
    return output

# def get_my_book():
#     return list(dbc.thangnq.find())

def get_all_book():
    return list(db.all.find())

get_all_books = get_all_book()

the_loai_ = [
    'tamli_kinangsong', 
    "/huyenbigiatuong", 
    "/kiemhiep",
    "/kinhte_quanly",
    "/makinhdi",
    "/makerting_banhang",
    "/tieuthuyettrungquoc",
    "/tieuthuyetphuongtay",
    "/trinhtham_hinhsu",
    "/truyenngan_ngontinh",
    "/truyentranh",
    "/vanhocvietnam"
    ]

xemnhieu=sortt()
data=get_book('kiemhiep')
@app.route('/', methods=['GET'])
def index():
    i=0
    top_xemnhieu = []
    for k in xemnhieu:
        i+=1
        top_xemnhieu.append(k)
        if i>20: 
            return render_template('index.html',book=top_xemnhieu)

@app.route('/', methods=['POST'])
def index____():
    session['key']=request.form.get("searchs")
    return redirect('/search')

@app.route('/search', methods=['GET'])
def index_______():
    if session['key'] != None:
        a = convert(session['key']).lower()
        session['key'] = None
    else:
        a = convert(session['name_searchs']).lower()
        session['name_searchs'] = None
    datas = []
    for v in get_all_book():
        b = convert(v['name']).lower()
        if a in b:
            datas.append(v)
    return render_template('search_home.html', datas=datas)

@app.route('/search', methods=['POST'])
def post_food___():
    session['name_searchs'] = request.form.get('searchss')
    return redirect('/search')

@app.route("/<the_loai__>")
def danhmuc_(the_loai__):
    data=get_book(the_loai__)
    return render_template("danhmuc.html",books=data, a=the_loai__)

# @app.route("/<the_loai__>", methods=['POST'])
# def danhmuc__(the_loai__):
#     session['name_searchs'] = request.form.get('searchsss')
#     return redirect('/search')

@app.route('/signup')
def sign_up_():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def post_signup():
    error = None
    username_signup= request.form.get("user")
    password_signup= request.form.get("pass")
    password_again_signup= request.form.get("pass_again")
    for v in get_all_signup():
        if v['username'] ==  username_signup:
            error = 'Tên đăng nhập đã tồn tại, vui lòng nhập lại!'
            return render_template('signup.html', error=error)
        if password_signup != password_again_signup:
            error = 'Password không trùng khớp, vui lòng nhập lại!'
            return render_template('signup.html', error=error)
        if ' ' in username_signup:
            error = 'Tên đăng nhập không được có dấu cách (space)), vui lòng nhập lại!'
            return render_template('signup.html', error=error)
        if convert(username_signup) != username_signup:
            error = 'Tên đăng nhập không được có dấu, vui lòng nhập lại!'
            return render_template('signup.html', error=error)
    client.dangki.signup.insert_one({'username':username_signup, 'password':password_signup})
    client.my_book[username_signup]
    return redirect('/signup/success')

@app.route('/signup/success')
def sign_up__():
    return render_template('signupsuccess.html')

@app.route('/login', methods=['GET'])
def get_login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def post_login():
    error = None
    session['username_login']= request.form.get("usernames")
    password_login= request.form.get("passwords")
    for v in get_all_signup():
        if v['username'] == session['username_login'] and v['password']== password_login:       
            return redirect('/my_book')
        else:    
            error = 'Tên người dùng hoặc mật khẩu sai, vui lòng đăng nhập lại!'
    return render_template('login.html', error=error)
    # return password_login

@app.route('/my_book', methods=['GET'])
def index_():
    return render_template('all_my_book.html', data=list(dbc[session['username_login']].find()))

@app.route('/my_book', methods=['POST'])
def post_food__():
    name_search = request.form.get('searchs')
    a = convert(name_search).lower()
    data = []
    for v in get_all_book():
        b = convert(v['name']).lower()
        if a in b:
            data.append(v)
    # return data[0]['name']
    return render_template('all_my_search.html',data=data)

@app.route('/my_book/<id_book>')
def aidi(id_book):
    for v in list(dbc[session['username_login']].find()):
        if str(v['_id'])==id_book:
            return render_template("update_book.html", V=v)

@app.route('/my_book/<id_book>', methods=['POST'])
def post_food(id_book):
    last_reading_day_update = request.form.get('last_reading_days')
    page_update = request.form.get('pages')
    note_update= request.form.get('notes')
    # note_update_2 = note_update + db.thangnq.find({'_id':ObjectId(id_book)})['note']
    db.thangnq.update_one({'_id':ObjectId(id_book)},{'$set':{'last_reading_day':last_reading_day_update}})
    db.thangnq.update_one({'_id':ObjectId(id_book)},{'$set':{'page':page_update}})
    db.thangnq.update_one({'_id':ObjectId(id_book)},{'$set':{'note':note_update}})
    return render_template('all_my_book.html', data=glist(dbc[session['username_login']].find()))

# @app.route('/tim_kiem')
# def index__():
#     return render_template('search.html')

# @app.route('/tim_kiem', methods=['POST'])
# def post_food__():
#     name_search = request.form.get('searchs')
#     a = convert(name_search).lower()
#     data = []
#     for v in get_all_book():
#         b = convert(v['name']).lower()
#         if a in b:
#             data.append(v)
#     # return data[0]['name']
#     return render_template('all_my_search.html',data=data)

@app.route('/my_book/add/<id_book_all>')
def aidi_add(id_book_all):
    for k in get_all_books:
        if str(k['_id'])==id_book_all:
            return render_template("add_book.html", K=k)

@app.route('/my_book/add/<id_book_all>', methods=['POST'])
def post_food_add(id_book_all): 
    s = request.form.get('start_dayss')
    p = request.form.get('pagess')
    n= request.form.get('notess')
    for k in get_all_books:
        if str(k['_id'])==id_book_all:
            b=k
    dbc[session['username_login']].insert_one({'user':session['username_login'],'book':b['name'],'online':b['link_online'],'start_day':s,'end_day':'','last_reading_day':s,'page':p,'note':n})
    return redirect('/my_book')

@app.route('/logout')
def logout():
   # remove the username from the session if it is there
   session.pop('username_login', None)
   return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)
