
from model.contact import Contact

def test_delete_contact(app):
    if app.contacts.count() == 0:
        app.contacts.create(Contact(firstname='test'))
    old_contact = app.contacts.get_contact_list ()
    app.contacts.delete_first_contact()
    new_contact = app.contacts.get_contact_list ()
    assert len ( old_contact - 1 ) == len ( new_contact )
    old_contact[0:1] = []
    assert old_contact == new_contact
