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


    @staticmethod
    def get_list_of_all():
        with open("contacts.pickle", "rb") as f:
            pickle.load(f)
            return f


    def edit_contact(self):
        pass

    
    @staticmethod
    def save_contact_to_file():
        with open("contacts.pickle", "wb") as f:
            pickle.dump(Contact.contacts, f)


    @classmethod
    def find_contact_by_name(cls, name):
        contacts_lst = cls.get_list_of_all()
        for contact in contacts_lst:
            if contact.name == name:
                return contact


    @classmethod
    def find_contact_by_email(cls, email):
        contacts_lst = cls.get_list_of_all()
        for contact in contacts_lst:
            if contact.email == email:
                return contact


    def group_contacts_into_catogories(self):
        pass


    @classmethod
    def delete_contact(cls, name):
        del cls.find_contact_by_name(name)