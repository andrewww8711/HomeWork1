# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application
from model.group import Group


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_homeworkone(app):
        app.session.login(username="admin", password="secret")
        app.group.create(Group(name="homework1", header="homework12", footer="homework13"))
        app.session.logout()


def test_empty_group_homeworkone(app):
        app.session.login(username="admin", password="secret")
        app.group.create(Group(name="", header="", footer=""))
        app.session.logout()