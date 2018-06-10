from model.group import Group
from random import randrange


def test_modify_group_name(app, db, json_groups, check_ui):
    group = json_groups
    if len(db.get_group_list()) == 0:
       app.group.create(group)
    old_groups = db.get_group_list()
    index = randrange(len(old_groups))
    group.id = old_groups[index].id
    app.group.modify_group_by_id(group.id, group)
    new_groups = db.get_group_list()
    old_groups[index] = group
    assert len(old_groups) == app.group.count()
    assert sorted(old_groups, key=Group.id_id_max) == sorted(new_groups, key=Group.id_id_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_id_max) == sorted(app.group.get_group_list(), key=Group.id_id_max)


