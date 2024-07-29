"""
Lab Excercise 1: Question 7
"""

"""
Declare a list/tuple containing all the twelve months. Write a Python program
that converts a month name entered via the Python console to the number
of days in that month (Consider leap year as well the code):
"""


def is_leap_year(year):
    # Check if the year is a leap year
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def get_days_in_month(month, year):
    # List of month names and days in each month (non-leap year)
    months = (
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    )
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Get the index of the month
    month = month.capitalize()  # Ensure case-insensitive comparison
    if month in months:
        index = months.index(month)
        # Adjust for leap year if February
        if index == 1 and is_leap_year(year):
            return 29
        return days_in_month[index]
    else:
        return None  # In case the month name is invalid


def get_days_in_month_by_input():
    # Get user input for month and year
    month_input = input("Enter the name of the month: ")
    year_input = int(input("Enter the year: "))

    # Get the number of days in the specified month and year
    days = get_days_in_month(month_input, year_input)

    # Output the result
    if days is not None:
        print(f"The number of days in {month_input} {year_input} is {days}.")
    else:
        print("Invalid month name entered.")
