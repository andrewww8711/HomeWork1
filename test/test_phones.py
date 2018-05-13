import re

def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)

def test_phons_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.homephone == contact_from_edit_page.homephone
    assert contact_from_view_page.cellphone == contact_from_edit_page.cellphone
    assert contact_from_view_page.workphone == contact_from_edit_page.workphone

def test_emails_on_home_page(app):
    emails_from_home_page = app.contact.get_contact_list()[0]
    emails_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert emails_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(emails_from_edit_page)



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