# -*- coding: utf-8 -*-
"""
    Views
    ~~~~~~~~~~~~~~

    Controller functions for each page.
    All the requests to the server are processed here.

    :copyright: (c) 2014 by Dario Coco
    :license: GPLv3, see LICENSE for more details.
"""
from flask import request, redirect, url_for, \
     render_template, flash, jsonify
from addressbook import app, db
from addressbook.forms import PhoneNumbersForm
from addressbook.models import Entry

'''
Homepage controller function.
Renders the home template.
'''
@app.route('/')
def home():
    return render_template('home.html')

'''
Get contacts page controller function.
Hits the database with a like case-insensitive query.
Accepts a search_txt parameter. Returns a JSON object.
'''
@app.route('/get_contacts', methods=['GET'])
def get_contacts():
    search_txt = request.args.get('search_txt')
    query_string = "%"+search_txt+"%"
    entries = Entry.query.filter((Entry.first_name.ilike(query_string))|\
                                 (Entry.last_name.ilike(query_string))|\
                                 (Entry.phone_number.ilike(query_string)))
    resp = jsonify(entries=[entry.to_dict() for entry in entries.all()])
    return resp


'''
Add contact page controller function.
GET:shows an empty form
POST: When form is submitted, fields are validated (see the models module).
'''
@app.route('/add', methods=['GET','POST'])
def add_entry():
    form = PhoneNumbersForm()
    if form.validate_on_submit():
        entry = Entry(form.first_name.data, form.last_name.data, form.phone_number.data)
        db.session.add(entry)
        db.session.commit()
        flash('New entry was successfully posted')
        return redirect(url_for('home'))
    return render_template('add.html', form=form)

'''
Edit entry page controller function.
GET: retrieves the entry by ID (parametric pretty URL)
POST: update the entry with the new date, validating the form on submit (see the models module)
'''
@app.route('/edit/<post_id>', methods=['GET','POST'])
def edit_entry(post_id):
    form = PhoneNumbersForm()
    entry = Entry.query.filter_by(id=post_id).first()
    if entry == None:
        return redirect(url_for('home'))
    if request.method == "GET":
        form.first_name.data = entry.first_name
        form.last_name.data = entry.last_name
        form.phone_number.data = entry.phone_number
    if form.validate_on_submit():  
        entry.first_name = form.first_name.data
        entry.last_name = form.last_name.data
        entry.phone_number = form.phone_number.data
        db.session.commit()
        #TODO: find a way to fade it out via javascript
        flash('New entry was successfully posted')
        return redirect(url_for('home'))
    return render_template('edit.html', post_id=post_id, form=form)
