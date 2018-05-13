from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create_address_book(self, contact):
        wd = self.app.wd
        self.open_home_page()
        self.open_address_book_page()
        self.fill_contact_form(contact)
        # submit the form
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.homephone)
        self.change_field_value("mobile", contact.cellphone)
        self.change_field_value("email", contact.email)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_index(index)
        wd.find_element_by_xpath(".//*[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def modify_first_contact(self, new_group_data):
        self.modify_contact_by_index(0, new_group_data)

    def modify_contact_by_index(self, index, new_group_data):
        wd = self.app.wd
        self.open_home_page()
        self.edit_random_contact(index)
        # modify contact form
        self.fill_contact_form(new_group_data)
        # submit the form
        wd.find_element_by_xpath(".//*[@id='content']/form[1]/input[22]").click()
        self.contact_cache = None

    def edit_random_contact(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath(".//table[@id='maintable']/tbody/tr/td[8]/a/img")[index].click()

    def open_address_book_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("addressbook/") and len(wd.find_elements_by_css_selector(".left input[value='Send e-Mail']")) > 0):
            wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                last_name = element.find_element_by_css_selector("tr > td:nth-child(2)").text
                first_name = element.find_element_by_css_selector("tr > td:nth-child(3)").text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(Contact(firstname=first_name, lastname=last_name, id=id))
            return list(self.contact_cache)

