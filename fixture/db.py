import pymysql.cursors
from model.group import Group
from model.contact import Contact
import re

class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password)
        self.connection.autocommit(True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list where deprecated = '0000-00-00 00:00:00'")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=re.sub("\s+", " ", name).strip(),
                                  header=re.sub("\s+", " ", header).strip(), footer=re.sub("\s+", " ", footer).strip()))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, home, mobile, email, email2, email3, work, address from addressbook "
                           "where deprecated = '0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, homephone, cellphone, email, email2, email3, workphone, address) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname,
                                    homephone=homephone, cellphone=cellphone,email=email, email2=email2,
                                    email3=email3, workphone=workphone, address=address))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()
