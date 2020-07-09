# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):

    app.contact.create( Contact( firstname ='anna', middlename =' alex',
                                 lastname = ' koz', nickname = ' an ', title = 'no', company = 'no',
                                 address = 'min', home='none', mobile = ' 35661', work = 'not',
                                 fax = ' 64131ftbr', email = ' uhui46@iby', email2='iuhi@jiyg', email3 = 'gugu@545trb',
                                 homepage = 'yuuh ', address2='ugy', phone2 = 'ugu', notes = 'ukhi' ) )




