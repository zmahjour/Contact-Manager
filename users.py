import pickle

class User:

    users = []   

    def __init__(self, username, password):
        self.username = username
        self.password = password


    @classmethod
    def create_account(cls, username, password):
        new_user = cls(username, password)
        cls.users.append(new_user)


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


    def modify_account(self, username, password):
        self.username = username
        self.password = password


    def save_user(self):
        pass



