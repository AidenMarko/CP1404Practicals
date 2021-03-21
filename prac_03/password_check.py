min_length = 10


def main():
    print("Please enter a valid password")
    print("Your password must be at least", min_length, "characters long")
    password = get_password()
    password_print(password)
    print("\nPassword Accepted")


def get_password():
    password = input("> ")
    while not check_password(password):
        print("Invalid password!")
        password = input("> ")
    return password


def password_print(password):
    password_length = len(password)
    for i in range(0, password_length, 1):
        print("*", end="")


def check_password(password):
    password_length = len(password)
    if password_length < min_length:
        return False
    else:
        return True


main()
