# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_address_book(app):
    old_contact = app.contact.get_contact_list()
    contact = Contact(firstname="John", lastname="Smith", title="QA Engineer", company="AAA", address="123 main street", homephone="123456", cellphone="1234567",
                                        email="test@mail.com")
    app.contact.create_address_book(contact)
    assert len(old_contact) + 1 == app.contact.count()
    new_contact = app.contact.get_contact_list()
    old_contact.append(contact)
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)


#def test_empty_add_address_book(app):
    #old_contact = app.contact.get_contact_list()
    #contact = Contact(firstname="", lastname="", title="", company="", address="", homephone="", cellphone="",
    #                                   email="")
    #app.contact.create_address_book(contact)
    #assert len(old_contact) + 1 == app.contact.count()
    #new_contact = app.contact.get_contact_list()
    #old_contact.append(contact)
    #assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)

