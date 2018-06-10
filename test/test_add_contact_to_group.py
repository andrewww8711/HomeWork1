from model.group import Group
from random import randrange
import random
from fixture.orm import ORMFixture

def test_add_contact_to_group(app, db, json_groups,json_contacts):
    random_group = random.choice(db.get_group_list())
    contacts_out_of_group = db.get_contacts_not_in_group(random_group)
    if len(contacts_out_of_group) == 0:
        contacts_in_group = db.get_contacts_in_group(random_group)
        random_contact = random.choice(contacts_in_group)
        app.contact.delete_contact_from_group(random_contact.id, random_group.id)
    random_contact_out_of_group = random.choice(contacts_out_of_group)
    app.contact.add_contact_to_group(random_contact_out_of_group.id, random_group.id)
    assert random_contact_out_of_group in db.get_contacts_in_group(random_group)




