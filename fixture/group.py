

class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text ( "groups" ).click ()

    def create(self, group):
        wd = self.app.wd
        self.app.open_home_page ( )
        # init gpoup creation
        wd.find_element_by_name ( "new" ).click ()
        # fill group form
        wd.find_element_by_name ( "group_name" ).click ()
        wd.find_element_by_name ( "group_name" ).clear ()
        wd.find_element_by_name ( "group_name" ).send_keys ( group.name )
        wd.find_element_by_name ( "group_header" ).click ()
        wd.find_element_by_name ( "group_header" ).clear ()
        wd.find_element_by_name ( "group_header" ).send_keys ( group.header )
        wd.find_element_by_name ( "group_footer" ).click ()
        wd.find_element_by_name ( "group_footer" ).clear ()
        wd.find_element_by_name ( "group_footer" ).send_keys ( group.footer )
        # submit group creation
        wd.find_element_by_name("submit" ).click()
        self.app.retern_to_groups_page()

    def delete_first_group(self):
        wd = self.app.wd
        self.app.open_home_page ()
        #select first group
        wd.find_element_by_name ( "selected[]" ).click ()
        #submit deletion
        wd.find_element_by_name ( "delete" ).click()
        self.app.retern_to_groups_page ()

    def edit_group(self):
        wd = self.app.wd
        self.app.open_home_page ()
        # select group
        wd.find_element_by_name ( "selected[]" ).click ()
        # editing
        wd.find_element_by_name ( "Edet group" ).click ()
        wd.find_element_by_name ( "group_name" ).click ()
        wd.find_element_by_name ( "group_name" ).clear ()
        wd.find_element_by_name ( "group_name" ).send_keys ( "koolh" )
        wd.find_element_by_name ( "group_header" ).click ()
        wd.find_element_by_name ( "group_header" ).clear ()
        wd.find_element_by_name ( "group_header" ).send_keys ( "lfgolsfpg" )
        wd.find_element_by_name ( "group_footer" ).click ()
        wd.find_element_by_name ( "group_footer" ).clear ()
        wd.find_element_by_name ( "group_footer" ).send_keys ( "klfkjp" )
        wd.find_element_by_name ( "update" ).click ()
        self.app.retern_to_groups_page ()

    def retern_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()