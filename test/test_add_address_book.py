# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_phone(prefix):
    digits = string.digits + "-" * 2
    return prefix + "".join([random.choice(digits) for i in range(10)])


def email(prefix, maxlen):
    symbols = string.ascii_letters + "@" + "."
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname="", lastname="", title="", company="", address="", homephone="", cellphone="", email="", email2="", email3="")] + [
        Contact(firstname=random_string("firstname", 10), lastname=random_string("lastname", 10),
                title=random_string("title", 20), company=random_string("company", 20),address=random_string("address", 20),
                homephone=random_phone("homephone"), cellphone=random_phone("cellphone"),
                email=email("email", 20), email2=email("email2", 20), email3=email("email3", 20))
        for i in range(5)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_address_book(app,  contact):
    old_contact = app.contact.get_contact_list()
    app.contact.create_address_book(contact)
    assert len(old_contact) + 1 == app.contact.count()
    new_contact = app.contact.get_contact_list()
    old_contact.append(contact)
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)

