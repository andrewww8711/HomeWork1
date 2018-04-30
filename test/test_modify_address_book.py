from model.contact import Contact


def test_modify_contact_name(app):
    app.contact.modify_first_contact(Contact(firstname="John_modified", lastname="Smith_modified"))


def test_modify_contact_address(app):
    app.contact.modify_first_contact(Contact(address="1111 California Street"))
