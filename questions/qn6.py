"""
Lab Excercise 1: Question 6
"""

"""
Question: Write a Python program to read a four-digit number and find its
(a) Sum of digits
(b) Reverse
"""


def processFourDigitNumber():
    # Get the four-digit number from the user
    fourDigitNumber: int = int(input("Enter a four-digit number: "))
    if fourDigitNumber < 1000 or fourDigitNumber > 9999:
        print("The number is not a four-digit number")
    else:
        # Get the sum of digits
        sumOfDigits: int = 0
        for digit in str(fourDigitNumber):
            sumOfDigits += int(digit)

        # Get the reverse of the number
        reverseNumber: int = int(str(fourDigitNumber)[::-1])

        print(f"Sum of digits: {sumOfDigits}")
        print(f"Reverse: {reverseNumber}")
