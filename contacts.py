import pickle
from users import User

class Contact:

    contacts = []

    def __init__(self, name, email, phone, owner_user: User):
        self.name = name
        self.email = email
        self.phone = phone
        self.owner_user = owner_user


    @classmethod    
    def add_contact(cls, name, email, phone):
        new_contact = cls(name, email, phone)
        cls.contacts.append(new_contact)


    @classmethod
    def edit_contact(self):
        pass


    def delete_contact(self):
        pass

    @staticmethod
    def save_contact():
        with open("contacts.pickle", "wb") as f:
            pickle.dump(Contact.contacts, f)


    def search_contact_by_name(self):
        pass


    def search_contact_by_email(self):
        pass


    def group_contacts_into_catogories(self):
        pass