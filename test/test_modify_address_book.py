from model.contact import Contact


def test_modify_contact_name(app):
    if app.contact.count() == 0:
        app.contact.create_address_book(Contact(firstname="test"))
    app.contact.modify_first_contact(Contact(firstname="John_modified", lastname="Smith_modified"))


def test_modify_contact_address(app):
    if app.contact.count() == 0:
        app.contact.create_address_book(Contact(firstname="test"))
    app.contact.modify_first_contact(Contact(address="1111 California Street"))
