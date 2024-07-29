"""
Lab Excercise 1: Question 2
"""

# Given list A
A = ["abc", "xyz", "aba", "1221"]

# Get the strings and their indices from the given list whose first and last characters match
similarityList = [
    (idx, aString) for idx, aString in enumerate(A) if aString[0] == aString[-1]
]
