"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def main():
    score = float(input("Enter score: "))
    print(score_checker(score))


def score_checker(score):
    if score < 0:
        result = "Invalid score"
        return result
    else:
        if score > 100:
            result = "Invalid score"
            return result
        elif score >= 90:
            result = "Excellent"
            return result
        elif score >= 50:
            result = "Passable"
            return result
        elif score < 50:
            result = "Bad"
            return result


def random_score():
    generated_score = random.randint(1, 100)
    print("Random score is: {}".format(generated_score))
    print(score_checker(generated_score))


main()
random_score()
