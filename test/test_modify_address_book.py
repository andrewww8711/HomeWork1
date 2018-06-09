from model.contact import Contact
from random import randrange


def test_modify_contact_name(app, db, check_ui, json_contacts):
    contact = json_contacts
    if len(db.get_group_list()) == 0:
        app.contact.create_address_book(Contact(lastname="test"))
    old_contact = db.get_contact_list()
    index = randrange(len(old_contact))
    contact.id = old_contact[index].id
    app.contact.modify_contact_by_id(contact.id, contact)
    assert len(old_contact) == app.contact.count()
    new_contact = db.get_contact_list()
    old_contact[index] = contact
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contact, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),key=Contact.id_or_max)