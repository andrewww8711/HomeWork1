# -*- coding: utf-8 -*-
from model.group import Group


def test_homeworkone(app):
        app.group.create(Group(name="group name", header="header name", footer="footer name"))


def test_empty_group_homeworkone(app):
        app.group.create(Group(name="", header="", footer=""))
