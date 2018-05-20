# -*- coding: utf-8 -*-
from model.group import Group


def test_homeworkone(app, json_groups):
        group = json_groups
        old_groups = app.group.get_group_list()
        app.group.create(group)
        assert len(old_groups) + 1 == app.group.count()
        new_groups = app.group.get_group_list()
        old_groups.append(group)
        assert sorted(old_groups, key=Group.id_id_max) == sorted(new_groups, key=Group.id_id_max)
