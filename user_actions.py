from contacts import Contact
from users import User

def add_new_contact():
    name = input("name: ")
    email = input("email: ")
    phone = input("phone: ")
    Contact.add_contact(name, email, phone)


def edit_exist_contact():
    current_name = input("current name: ")
    name = input("name: ") or None
    email = input("email: ") or None
    phone = input("phone: ") or None
    Contact.edit_contact(current_name, name, email, phone)
    

def delete_exist_contact():
    name = input("name: ")
    Contact.delete_contact(name)


def view_all_contacts():
    pass


def search_contact():
    choice = input("search by 1.name or 2.email? (1 or 2)")
    if choice == "1":
        Contact.find_contact_by_name(input("name: "))
    elif choice == "2":
        Contact.find_contact_by_email(input("email: "))


def modify_exist_account():
    current_username = input("current username: ")
    username = input("username: ") or None
    password = input("password: ") or None
    User.modify_account(current_username, username, password)
