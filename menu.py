from menu.models import generate_menu_from_dict
from user_actions import add_new_contact, edit_exist_contact, delete_exist_contact, view_all_contacts, search_contact, modify_exist_account
from users import User


def sign_up():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    User.create_account(username, password)


def log_in():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    User.authenticate_account(username, password)
    generate_menu_from_dict(second_menu)


first_menu = {
    "name": "Contact Manager",
    "children": [
        {
            "name": "Sign up",
            "action": sign_up,
        },
        {
            "name": "Sign in",
            "action": log_in
        },
    ],
}


second_menu = {
    "name": "Manage Contacts",
    "children": [
        {
            "name": "Add contact",
            "action": add_new_contact,
        },
        {
            "name": "Edit contact",
            "action": edit_exist_contact,
        },
        {
            "name": "Delete contact",
            "action": delete_exist_contact,
        },
        {
            "name": "View all contacts",
            "action": view_all_contacts,
        },
        {
            "name": "Search contact",
            "action": search_contact,
        },
        {
            "name": "Quit",
            "action": exit
        },
    ],
    "name": "Modify account",
    "action": modify_exist_account
}


menu = generate_menu_from_dict(first_menu, parent=None)
menu()