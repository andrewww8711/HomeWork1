# -*- coding: utf-8 -*-
from model.group import Group


def test_homeworkone(app):
        app.session.login(username="admin", password="secret")
        app.group.create(Group(name="homework1", header="homework12", footer="homework13"))
        app.session.logout()


def test_empty_group_homeworkone(app):
        app.session.login(username="admin", password="secret")
        app.group.create(Group(name="", header="", footer=""))
        app.session.logout()
