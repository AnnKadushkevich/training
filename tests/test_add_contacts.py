# -*- coding: utf-8 -*-

import pytest
from model.contact import Contact
from fixture.application import Application

@pytest.fixture
def app():
    fixture = Application()
    request.addfinalizer ( fixture.destroy )
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create( Contact( firstname ='anna', middlename =' alex',
                                 lastname = ' koz', nickname = ' an ', title = 'no', company = 'no',
                                 address = 'min', home='none', mobile = ' 35661', work = 'not',
                                 fax = ' 64131ftbr', email = ' uhui46@iby', email2='iuhi@jiyg', email3 = 'gugu@545trb',
                                 homepage = 'yuuh ', address2='ugy', phone2 = 'ugu', notes = 'ukhi' ) )
    app.session.logout ( )



