"""
CP1404/CP5632 Practical
Do-from-scratch - Emails
"""

def main():
    email = input("Email: ")
    while email != "":
        name = get_name(email)
        print(input("Is your name {}? (y/n) ".format(name)))


def get_name(email):
    email = email.split("@")
    print(email)
    name = email[0]
    name = name.split(".")
    print(name)
    return name


main()
