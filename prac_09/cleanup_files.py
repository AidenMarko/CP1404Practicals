"""
CP1404/CP5632 Practical
Cleanup Files
"""

import os

def main():
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))
        for filename in filenames:
            new_name = get_fixed_filename(filename)
            print("Changing file {} to {}".format(filename, new_name))
            os.rename(os.path.join(directory_name, filename), os.path.join(directory_name, new_name))


def get_fixed_filename(filename):
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    for character in new_name:
        if character.isupper():
            character = "_" + character

    return new_name


main()
