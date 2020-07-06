
def test_edit_contact(app):
    app.session.login ( username="admin", password="secret" )
    app.contacts.edit_contact()
    app.session.logout ()