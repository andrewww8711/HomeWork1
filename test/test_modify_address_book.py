from model.contact import Contact


def test_modify_contact(app):
    app.contact.modify_first_contact(Contact(firstname="John_modified", lastname="Smith_modified", title="QA Engineer_modified", company="AAA_modified", address="123 main street_modified", homephone="123456_modified", cellphone="1234567_modified",
                                        email="modified_test@mail.com"))
