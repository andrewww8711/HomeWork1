from model.contact import Contact


def test_modify_contact_name(app):
    old_contact = app.contact.get_contact_list()
    contact = Contact(firstname="test11", lastname="test")
    contact.id = old_contact[0].id
    if app.contact.count() == 0:
        app.contact.create_address_book(Contact(lastname="test"))
    app.contact.modify_first_contact(contact)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) == len(new_contact)
    old_contact[0] = contact
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)


#def test_modify_contact_address(app):
#    if app.contact.count() == 0:
#       app.contact.create_address_book(Contact(firstname="test"))
#   app.contact.modify_first_contact(Contact(address="1111 California Street"))
