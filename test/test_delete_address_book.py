from model.contact import Contact

def test_delete_address_book(app):
    old_contact = app.contact.get_contact_list()
    if app.contact.count() == 0:
        app.contact.create_address_book(Contact(firstname="test"))
    app.contact.delete_first_contact()
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) - 1 == len(new_contact)
    old_contact[0:1] = []
    assert old_contact == new_contact

