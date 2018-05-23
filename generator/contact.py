from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_phone(prefix):
    digits = string.digits + "-" * 2
    return prefix + "".join([random.choice(digits) for i in range(10)])


def email(prefix, maxlen):
    symbols = string.ascii_letters + "@" + "."
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname="", lastname="", title="", company="", address="", homephone="", cellphone="", email="", email2="", email3="")] + [
        Contact(firstname=random_string("firstname", 10), lastname=random_string("lastname", 10),
                title=random_string("title", 20), company=random_string("company", 20),address=random_string("address", 20),
                homephone=random_phone("homephone"), cellphone=random_phone("cellphone"),
                email=email("email", 20), email2=email("email2", 20), email3=email("email3", 20))
        for i in range(n)
]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))