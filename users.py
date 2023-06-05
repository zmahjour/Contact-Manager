import pickle


class User:

    users = []   

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.user_contacts = []


    @classmethod
    def create_account(cls, username, password):
        new_user = cls(username, password)
        cls.users.append(new_user)


    def authenticate_account(self):
        pass


    def modify_account(self):
        pass


    def save_user(self):
        pass



