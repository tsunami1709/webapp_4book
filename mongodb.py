import pymongo
from bson.objectid import ObjectId
client = pymongo.MongoClient("mongodb+srv://thangnq:12345678Abc@cluster0-zqxy8.mongodb.net/test?retryWrites=true&w=majority")

db = client.my_book

dbc= client.dangki

def get_all_signup():
    return list(dbc.signup.find())

dbb = client.all_book
def get_book(theloai):
    return list(dbb[theloai].find())
def sortt():
    return dbb.all.find().sort('reading')
# def insert_signup(username,password,number_phone):
#     db.signup.insert_one({'username': username, 'password': password,'numberphone':number_phone})

# print(get_all_signup())
# insert_signup('thangnq','12345678','0379850688')
# insert_signup('lien','12345678','03719850688')

# db.thangnq.insert_one({
#     'user':'thangnq',
#     'book':'Lối Sống Tối Giản Của Người Nhật',
#     'online':'https://sachvui.com/doc-sach/loi-song-toi-gian-cua-nguoi-nhat-sasaki-fumio/cau-truc-cuon-sach.html',
#     'start_day':'07/08/2019',
#     'end_day':'',
#     'last_reading_day':'08/08/2019',
#     'page':'23',
#     'note':['Chương 1 hay phết']
# }
# )
# db.foods.insert_one({'name':'com rang', 'price':30})

def get_my_book():
    return list(db.thangnq.find())

# def insert_book(user,book,online,start_day,end_day,last_reading_day,page,note):
#     db.thangnq.insert_one({
#     'user':user,
#     'book':book,
#     'online':online,
#     'start_day':start_day,
#     'end_day':end_day,
#     'last_reading_day':last_reading_day,
#     'page':page,
#     'note':note
# }

def delete_book_by_id(book_id):
    db.thangnq.delete_one({'_id':ObjectId(book_id)})


