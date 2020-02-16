from model.contact import Contact


def test_modify_contact_first_name(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(first_name="New first name"))
    app.session.logout()


def test_modify_contact_last_name(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(last_name="New last name"))
    app.session.logout()