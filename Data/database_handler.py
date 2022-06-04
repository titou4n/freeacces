from flask_pymongo import PyMongo

class DatabaseHandler():
  def create_person(self, mail:str, password:str):
    cluster.insert_one({"mail":"mail"},{"password":"password"})
   