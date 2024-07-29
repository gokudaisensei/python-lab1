"""
Lab Excercise 1: Question 5
"""

# Subpart A: range(1, 50)
evenNumListA: list[tuple] = [(x, x**2) for x in range(1, 50) if (x % 2 == 0)]

# Subpart B: range(1, 100)
evenNumListB: list[tuple] = [(x, x**2) for x in range(1, 100) if (x % 2 == 0)]
