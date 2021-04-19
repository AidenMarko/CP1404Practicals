"""CP1404/CP5632 Practical - guitar test."""

from prac_06.guitar import Guitar

def main():
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    fender = Guitar("Fender", 2000, 4000)

    print("Gibson L-5 CES get_age() - Expected 99. Got {}".format(gibson.get_age()))
    print("Fender get_age() - Expected 21. Got {}".format(fender.get_age()))
    print("Gibson L-5 CES is_vintage() - Expected True. Got {}".format(gibson.is_vintage()))
    print("Fender is_vintage() - Expected False. Got {}".format(fender.is_vintage()))


main()
