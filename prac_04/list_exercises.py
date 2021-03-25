"""
CP1404/CP5632 Practical
List Exercises
"""


def main():
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


main()
