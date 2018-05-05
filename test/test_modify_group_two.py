from model.group import Group


def test_modify_group_name(app):
    old_groups = app.group.get_group_list()
    group = Group(name="new group")
    group.id = old_groups[0].id
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.modify_first_group_two(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_id_max) == sorted(new_groups, key=Group.id_id_max)


#def test_modify_group_header(app):
#    old_groups = app.group.get_group_list()
#    if app.group.count() == 0:
#        app.group.create(Group(name="test"))
#    app.group.modify_first_group_two(Group(header="new header"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)
