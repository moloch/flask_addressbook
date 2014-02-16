"""
    Models
    ~~~~~~~~~~~~~~

    SQLAlchemy models
    

    :copyright: (c) 2014 by Dario Coco
    :license: GPLv3, see LICENSE for more details.
"""

from addressbook import db

'''
Represents an address book entry in the database.
A dictionary convertion method is provided to help with JSON serialization
'''
class Entry(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    phone_number = db.Column(db.String(80))
    
    def __init__(self, first_name, last_name, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        
    def to_dict(self):
        d = dict()
        d["id"] = str(self.id)
        d["first_name"] = str(self.first_name)
        d["last_name"] = str(self.last_name)
        d["phone_number"] = str(self.phone_number)
        return d

def create_db():
    db.create_all()
