"""
CP1404/CP5632 Practical
Colours in a dictionary
"""

COLOUR_TO_HEXADECIMAL = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "AntiqueWhite1": "	#ffefdb",
                         "AntiqueWhite2": "#eedfcc", "AntiqueWhite3": "#cdc0b0", "AntiquesWhite4": "#8b8378",
                         "aquamarine1": "#7fffd4", "aquamarine2": "	#76eec6", "aquamarine4": "#458b74",
                         "azure1": "#f0ffff"}
for key in COLOUR_TO_HEXADECIMAL:
    print(key, end=", ")

colour_name = input("\nInput a colour name: ")
while colour_name != "":
    if colour_name in COLOUR_TO_HEXADECIMAL:
        print(colour_name, "is", COLOUR_TO_HEXADECIMAL[colour_name])
    else:
        print("Invalid colour name")
    colour_name = input("Input a colour name: ")
print("Thank you")
