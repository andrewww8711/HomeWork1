from model.contact import Contact
from random import randrange


def test_modify_contact_name(app):
    if app.contact.count() == 0:
        app.contact.create_address_book(Contact(lastname="test"))
    old_contact = app.contact.get_contact_list()
    index = randrange(len(old_contact))
    contact = Contact(firstname="test11", lastname="test")
    contact.id = old_contact[index].id
    app.contact.modify_contact_by_index(index, contact)
    assert len(old_contact) == app.contact.count()
    new_contact = app.contact.get_contact_list()
    old_contact[index] = contact
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)


#def test_modify_contact_address(app):
#    if app.contact.count() == 0:
#       app.contact.create_address_book(Contact(firstname="test"))
#   app.contact.modify_first_contact(Contact(address="1111 California Street"))
