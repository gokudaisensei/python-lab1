"""
Lab Excercise 1: Question 9
"""

"""
Write a Python program to extract the rear elements from a tuple string
"""


def extract_last_characters(input_tuple):
    # Use list comprehension to get the last character of each string in the tuple
    print([string[-1] for string in input_tuple])


input_tuple = ("python", "learn", "includehelp")
