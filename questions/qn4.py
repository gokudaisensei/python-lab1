"""
Lab Excercise 1: Question 4
"""

# Given List
ListColour = ["Black", "Red", "Maroon", "Yellow"], [
    "000000",
    "FF0000",
    "800000",
    "FFFF00",
]

clrDictionary: dict[str, str] = {color: hexcode for color, hexcode in zip(*ListColour)}
