"""
CP1404/CP5632 Practical
Do-from-scratch - Emails
"""

NAME_TO_EMAIL = {}

def main():
    email = input("Email: ")
    while email != "":
        name = get_name(email)
        confirm_name(email, name)
        email = input("Email: ")
    print()
    for name, email in NAME_TO_EMAIL.items():
        print("{} ({})".format(name, email))


def confirm_name(email, name):
    name_conformation = input("Is your name {}? (Y/n) ".format(name))
    if name_conformation.lower() == "n" or name_conformation.lower() == "no":
        name = input("Name: ")
        NAME_TO_EMAIL[name] = email
    elif name_conformation.lower() == "y" or name_conformation.lower() == "" or name_conformation.lower() == "yes":
        NAME_TO_EMAIL[name] = email


def get_name(email):
    email = email.split("@")
    name = email[0]
    names = name.split(".")
    full_name = " ".join(names)
    full_name = full_name.title()
    return full_name


main()
