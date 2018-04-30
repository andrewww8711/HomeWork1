class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create_address_book(self, contact):
        self.open_address_book_page()
        wd = self.app.wd
        self.fill_contact_form(contact)
        # submit the form
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

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
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath(".//*[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()

    def modify_first_contact(self, new_group_data):
        wd = self.app.wd
        self.open_home_page()
        self.edit_first_contact()
        # modify contact form
        self.fill_contact_form(new_group_data)

        # submit the form
        wd.find_element_by_xpath(".//*[@id='content']/form[1]/input[22]").click()

    def edit_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_xpath(".//*[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()

    def open_address_book_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def open_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        self.open_address_book_page()
        return len(wd.find_elements_by_name("selected[]"))