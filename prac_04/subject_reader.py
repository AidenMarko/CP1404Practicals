"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    display_subject_details(data)


def display_subject_details(data):
    for i in range(0, 3, 1):
        subject = data[i][0][0]
        teacher = data[i][0][1]
        number_of_students = data[i][0][2]
        print("{} is taught by {:12s} and has {:3} students".format(subject, teacher, number_of_students))


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    list_of_parts = []
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        list_of_parts.append([parts])
        print(list_of_parts)
        print("----------")
    input_file.close()
    return list_of_parts


main()
