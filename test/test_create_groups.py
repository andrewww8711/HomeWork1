# -*- coding: utf-8 -*-
from model.group import Group
import pytest


def test_homeworkone(app, db, json_groups, check_ui):
        group = json_groups
        with py.test.allure.step('Given a group list')
        old_groups = db.get_group_list()
        app.group.create(group)
        # assert len(old_groups) + 1 == app.group.count()
        new_groups = db.get_group_list()
        old_groups.append(group)
        assert sorted(old_groups, key=Group.id_id_max) == sorted(new_groups, key=Group.id_id_max)
        if check_ui:
                assert sorted(new_groups, key=Group.id_id_max) == sorted(app.group.get_group_list(), key=Group.id_id_max)
