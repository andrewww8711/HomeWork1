from model.contact import Contact

def test_delete_address_book(app):
    if app.contact.count() == 0:
        app.contact.create_address_book(Contact(firstname="test"))
    app.contact.delete_first_contact()

