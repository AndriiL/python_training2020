from model.contact import Contact


def test_modify_contact_first_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="test_name"))
    app.contact.modify_first_contact(Contact(first_name="New first name"))


def test_modify_contact_last_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="test_name"))
    app.contact.modify_first_contact(Contact(last_name="New last name"))
