import pickle
from users import User

class Contact:

    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        #self.owner_user = owner_user


    @classmethod    
    def add_contact(cls, name, email, phone):
        new_contact = [cls(name, email, phone)]
        new_contacts_lst = cls.get_list_of_all() + new_contact
        cls.save_to_file(new_contacts_lst)


    @staticmethod
    def get_list_of_all():
        with open("./data/contacts.pickle", "rb") as f:
            list_of_all = pickle.load(f)
            return list_of_all


    @classmethod
    def edit_contact(cls, current_name, name, email, phone):
        obj = cls.find_contact_by_name(current_name)
        obj.name = name or obj.name
        obj.email = email or obj.email
        obj.phone = phone or obj.phone
        cls.delete_contact(current_name)
        cls.add_contact(obj.name, obj.email, obj.phone)

    
    @staticmethod
    def save_to_file(contacts_lst):
        with open("./data/contacts.pickle", "wb") as f:
            pickle.dump(contacts_lst, f)


    @classmethod
    def find_contact_by_name(cls, name):
        for contact in cls.get_list_of_all():
            if contact.name == name:
                return contact


    @classmethod
    def find_contact_by_email(cls, email):
        for contact in cls.get_list_of_all():
            if contact.email == email:
                return contact


    def group_contacts_into_catogories(self):
        pass


    @classmethod
    def delete_contact(cls, name):
        cls.get_list_of_all.remove(cls.find_contact_by_name)
        cls.save_to_file(cls.get_list_of_all())