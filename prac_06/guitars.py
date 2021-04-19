"""CP1404/CP5632 Practical - guitars."""

from prac_06.guitar import Guitar

def main():
    guitars = []
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = input("Cost: ")
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        name = input("Name: ")
    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        if guitar.is_vintage():
            print("Guitar {}: {} ({}), Worth $ {} (vintage)".format(i, guitar.name, guitar.year, guitar.cost))
        else:
            print("Guitar {}: {} ({}), Worth $ {}".format(i, guitar.name, guitar.year, guitar.cost))


main()
