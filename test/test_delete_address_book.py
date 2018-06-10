from model.contact import Contact
from random import randrange
import random
import time

def test_delete_address_book(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create_address_book(Contact(firstname="test"))
    old_contact = db.get_contact_list()
    contact = random.choice(old_contact)
    #index = randrange(len(old_contact))
    app.contact.delete_contact_by_id(contact.id)
    time.sleep(1)
    new_contact = db.get_contact_list()
    assert len(old_contact) - 1 == app.contact.count()
    old_contact.remove(contact)
    #old_contact[index:index+1] = []
    assert old_contact == new_contact
    if check_ui:
        assert sorted(new_contact, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
