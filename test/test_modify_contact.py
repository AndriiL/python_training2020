from model.contact import Contact


def test_modify_contact_first_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="test_name"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(first_name="New first name"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_modify_contact_last_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="test_name"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(last_name="New last name"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
