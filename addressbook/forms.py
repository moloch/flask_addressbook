"""
    Forms
    ~~~~~~~~~~~~~~

    Validation is provided for each column.
    

    :copyright: (c) 2014 by Dario Coco
    :license: GPLv3, see LICENSE for more details.
"""

import re
from flask_wtf import Form
from wtforms import TextField
from wtforms.validators import DataRequired, Regexp

# WTF Form to send a new entry data to our server
# It includes validation and CRSF token, because it extends the WTForms class Form
class PhoneNumbersForm(Form):

    # Regular expression to check this rule:

    # "a "+" followed by a nonempty group of digits, a space, a
    # nonempty group of digits, a space, a group of digits with at least 6
    # digits."

    _prog = re.compile(r"\+\d+\ \d+\ \d{6,}")

    # Form fields

    first_name = TextField('First name', validators=[DataRequired()])
    last_name = TextField('Last name', validators=[DataRequired()])
    phone_number = TextField('Phone number', validators=[Regexp(_prog)])