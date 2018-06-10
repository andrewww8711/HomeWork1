import re
from model.contact import Contact


def test_all_fields_on_home_page(app, db):
    len_contact_from_home_page = app.contact.get_contact_list()
    for index in range(len(len_contact_from_home_page)):
        contact_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)[index]
        contact_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)[index]
        assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_db)
        assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_db)
        assert contact_from_home_page.firstname == contact_from_db.firstname
        assert contact_from_home_page.lastname == contact_from_db.lastname
        assert contact_from_home_page.address_from_home_page == contact_from_db.address


#def test_all_fields_on_home_page(app):
#   contact_from_home_page = app.contact.get_contact_list()[0]
#    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
#    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
#    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)
#    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
#    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
#    assert contact_from_home_page.address == contact_from_edit_page.address

#def test_phons_on_contact_view_page(app):
    #contact_from_view_page = app.contact.get_contact_from_view_page(0)
    #contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    #assert contact_from_view_page.homephone == contact_from_edit_page.homephone
    #assert contact_from_view_page.cellphone == contact_from_edit_page.cellphone
    #assert contact_from_view_page.workphone == contact_from_edit_page.workphone

def clear(s):
    return re.sub("[()-]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x !="",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.cellphone, contact.workphone]))))

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))