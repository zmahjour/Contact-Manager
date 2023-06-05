import pickle


class Contact:

    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone


    @classmethod    
    def add_contact(cls, name, email, phone):
        new_contact = cls(name, email, phone)
        


    def edit_contact(self):
        pass


    def delete_contact(self):
        pass


    def save_contact(self):
        pass


    # def search_contact_by_name(self):
    #     pass


    # def search_contact_by_email(self):
    #     pass


    # def group_contacts_into_catogories(self):
    #     pass