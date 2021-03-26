"""
CP1404/CP5632 Practical
Quick Picks
"""

import random


def main():
    print("How many quick picks?")
    number_of_picks = int(input(">>> "))
    number_set = print_picks(number_of_picks)
    for group in number_set:
        for number in group:
            print(number, end=" ")
        print()


def print_picks(number_of_picks):
    number_set = []
    generated_number = random.randint(1, 45)
    for j in range(0, number_of_picks, 1):
        generated_set = []
        for i in range(0, 6, 1):
            while generated_number in generated_set:
                generated_number = random.randint(1, 45)
            generated_set.append(generated_number)
        generated_set.sort()
        number_set.append(generated_set)
    return number_set


main()
