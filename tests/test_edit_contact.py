from model.contact import Contact

def test_edit_contact(app):
    if app.contacts.count() == 0:
        app.contacts.create(Contact(firstname=''))

    app.contacts.edit_contact()
