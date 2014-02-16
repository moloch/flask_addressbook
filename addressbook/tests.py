# -*- coding: utf-8 -*-
"""
    Flask_addressbook Tests
    ~~~~~~~~~~~~

    Tests the addressbook application.

    :copyright: (c) 2014 by Dario Coco
    :license: GPLv3, see LICENSE for more details.
"""
import os
os.environ['DATABASE_URL'] = 'sqlite:///:memory:'
import unittest, json
from addressbook import app, db
from addressbook.models import Entry

class AddressbookTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        
    def test_add(self):
        data=dict(
           first_name="Dario",
           last_name="Coco",
           phone_number="+39 333 666666"
        )
        self.app.post('/add', data=data, follow_redirects=False)
        entry = Entry.query.filter_by(first_name="Dario").first()
        assert entry.first_name == data['first_name']
        assert entry.last_name == data['last_name']
        assert entry.phone_number == data['phone_number']
        rv = self.app.get('/get_contacts?search_txt=Dario')
        dict_rv = json.loads(rv.data)
        k = 'entries'
        assert len(dict_rv.keys()) == 1
        assert len(dict_rv['entries']) == 1
        result = dict_rv[k][0]
        assert len(result.keys()) == 4
        assert result['id'] == '1'
        assert result['first_name'] == entry.first_name
        assert result['last_name'] == entry.last_name
        assert result['phone_number'] == entry.phone_number
        

if __name__ == '__main__':
    unittest.main()
