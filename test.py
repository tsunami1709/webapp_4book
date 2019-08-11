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

print(get_book('tamly_kynangsong'))