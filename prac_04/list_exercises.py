"""
CP1404/CP5632 Practical
List Exercises
"""


def main():
    if check_username():
        numbers = get_numbers()
        print_numbers(numbers)


def get_numbers():
    numbers = []
    for i in range(0, 5, 1):
        number = float(input("Number: "))
        numbers = numbers + [number]
    return numbers


def print_numbers(numbers):
    print("The first number is {}".format(numbers[0]))
    print("The last number is {}".format(numbers[-1]))
    print("The smallest number is {}".format(min(numbers)))
    print("The largest number is {}".format(max(numbers)))
    average = sum(numbers)/len(numbers)
    print("The average of the numbers is {}".format(average))


def check_username():
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    print("Enter your username: ")
    username = input(">>> ")
    if username in usernames:
        print("Username Accepted")
        return True
    else:
        print("Username Declined")
        return False


main()
