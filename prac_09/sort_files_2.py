"""
CP1404/CP5632 Practical
Sort Files V2
"""

import os
import shutil

def main():
    os.chdir("FilesToSort")
    extensions = {}
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue
        extension = filename.split('.')[-1]
        if extension not in extensions:
            folder_name = input("What category would you like to sort {} files into? ".format(extension))
            extensions[extension] = folder_name
            try:
                os.mkdir(folder_name)
            except FileExistsError:
                pass
        shutil.move(filename, "{}/{}".format(extensions[extension], filename))
        print("Copying {} to folder {}".format(filename, extensions[extension]))


main()
