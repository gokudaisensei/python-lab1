"""
Lab Excercise 1: Question 1
"""

from random import randint

# Declaring a python list
qnList: list[int] = [randint(1, 50) for _ in range(15)]

# Subpart A: Sum all the items of the list
qnListSum: int = sum(qnList)

# Subpart B: Multiply all the items of the list
qnListMultiply: list[int] = [randint(2, 4) * x for x in qnList]

# Subpart C: Get the largest number from the list
qnListLargestNumber: int = max(qnList)

# Subpart D: Get the smallest number from the list
qnListSmallestNumber: int = min(qnList)
