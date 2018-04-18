# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from model.contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_address_book(app):
        app.session.login(username="admin", password="secret")
        app.contact.create_address_book(Contact(firstname="Ivan", lastname="Ivanov", title="QA Engineer", company="Google", address="123 main street", homephone="123456", cellphone="1234567",
                                        email="test@mail.com"))
        app.session.logout()


def test_empty_add_address_book(app):
        app.session.login(username="admin", password="secret")
        app.contact.create_address_book(Contact(firstname="", lastname="", title="", company="", address="", homephone="", cellphone="",
                                        email=""))
        app.session.logout()