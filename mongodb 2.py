import pymongo
# from bson.objectid import ObjectId
client = pymongo.MongoClient("mongodb+srv://thangnq:12345678Abc@cluster0-zqxy8.mongodb.net/test?retryWrites=true&w=majority")

db= client.dangki

def get_all_signup():
    return list(db.signup.find())
# def insert_signup(username,password,number_phone):
#     db.signup.insert_one({'username': username, 'password': password,'numberphone':number_phone})

# print(get_all_signup())
# insert_signup('thangnq','12345678','0379850688')
# insert_signup('lien','12345678','03719850688')
