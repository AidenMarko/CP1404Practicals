"""
CP1404/CP5632 Practical
Sort Files V1
"""

import os
import shutil


def main():
    extension_list = ["xlsx", "xls", "txt", "png", "jpg", "gif", "docx", "doc"]
    os.chdir('FilesToSort')
    for extension in extension_list:
        try:
            os.mkdir(extension)
        except FileExistsError:
            continue
        for filename in os.listdir('.'):
            if filename.endswith(extension):
                try:
                    shutil.move(filename, extension + "/" + filename)
                except shutil.Error:
                    continue
                print("Copying {} to folder {}".format(filename, extension))


main()
