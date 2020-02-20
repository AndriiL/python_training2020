# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(first_name="first_name", last_name="last_name", address="address", email="email"))


def test_add_empty_contact(app):
    app.contact.create(Contact(first_name="", last_name="", address="", email=""))

