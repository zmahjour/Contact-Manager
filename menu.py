from menu.models import generate_menu_from_dict

first_menu = {
    "name": "Contact Manager",
    "children": [
        {
            "name": "Sign up",
            "action": create_account,
        },
        {
            "name": "Sign in",
            "action": login
        },
    ],
}



second_menu = {
    "name": "Manage Contacts",
    "children": [
        {
            "name": "Add contact",
            "action": add_contact,
        },
        {
            "name": "Edit contact",
            "action": edit_contact,
        },
        {
            "name": "Delete contact",
            "action": delete_contact,
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
            "name": "Sign in",
            "action": login
        },
    ],
    "name": "Modify account"
    "action": modify_account
}

