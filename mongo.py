
from pymongo import MongoClient
import pprint as pretty
import certifi

ca = certifi.where()

client = MongoClient("mongodb+srv://Ayelet:Ayelet25@pythonatdell."
                     "go6jh.mongodb.net/PythonAtDell?retryWrites=true&w=majority", tlsCAFile=ca)
db = client.test
server_status = db.command("serverStatus")
pretty.pprint(server_status)

print("This is the end of the file.")


def first_func():
    print("This is a function")


def second_func():
    print('Second func')


def third_func():
    print("Third func")
