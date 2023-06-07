import pickle

class User:

    def __init__(self, username, password):
        self.username = username
        self.password = password


    @classmethod
    def create_account(cls, username, password):
        new_user = [cls(username, password)]
        new_users_lst = cls.get_list_of_all() + new_user
        cls.save_to_file(new_users_lst)


    @staticmethod
    def get_list_of_all():
        try:
            with open("~/Samane/Python_VM/Maktab/W9/HW/Contact-Manager/data/users.pickle", "rb") as f:
                list_of_all = pickle.load(f)
                return list_of_all or []
        except:
            return []


    def authenticate_account(self, username, password):
        try:
            assert username == self.username
            try:
                assert password == self.password
                return True
            except:
                return "The password is wrong"
        except:
            return "The username is wrong"


    @classmethod
    def modify_account(cls, current_username, username, password):
        obj = cls.find_contact_by_username(current_username)
        obj.username = username or obj.username
        obj.password = password or obj.password
        cls.delete_user(current_username)
        cls.create_account(obj.username, obj.password)


    @classmethod
    def find_contact_by_username(cls, username):
        for user in cls.get_list_of_all():
            if user.username == username:
                return user


    @staticmethod
    def save_to_file(users_lst):
        with open("~/Samane/Python_VM/Maktab/W9/HW/Contact-Manager/data/users.pickle", "wb") as f:
            pickle.dump(users_lst, f)


    @classmethod
    def delete_user(cls, username):
        cls.get_list_of_all.remove(cls.find_user_by_username)
        cls.save_to_file(cls.get_list_of_all())



