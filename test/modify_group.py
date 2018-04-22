from model.group import Group


def test_modify_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(name="modified group name", header="modified header name", footer="modified footer name"))
    app.session.logout()