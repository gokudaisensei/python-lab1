"""
Lab Excercise 1: Question 7
"""

"""
Question: Write a program to find the area of a triangle. Then find the area of two
arbitrary triangles by entering the three sides both using the input function
(input()). Print the total area enclosed by both triangles and each triangle’s
contribution (%) towards it.
"""

import math


def calculate_area(a, b, c):
    # Calculate the semi-perimeter
    s = (a + b + c) / 2
    # Calculate the area using Heron's formula
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area


def find_triangle_areas_and_contributions():
    # Input for the first triangle
    a1 = float(input("Enter the first side of the first triangle: "))
    b1 = float(input("Enter the second side of the first triangle: "))
    c1 = float(input("Enter the third side of the first triangle: "))

    # Input for the second triangle
    a2 = float(input("Enter the first side of the second triangle: "))
    b2 = float(input("Enter the second side of the second triangle: "))
    c2 = float(input("Enter the third side of the second triangle: "))

    # Calculate areas
    area1 = calculate_area(a1, b1, c1)
    area2 = calculate_area(a2, b2, c2)

    # Total area
    total_area = area1 + area2

    # Percentage contributions
    percent1 = (area1 / total_area) * 100
    percent2 = (area2 / total_area) * 100

    # Print results
    print(f"Area of the first triangle: {area1:.2f}")
    print(f"Area of the second triangle: {area2:.2f}")
    print(f"Total area enclosed by both triangles: {total_area:.2f}")
    print(f"Contribution of the first triangle: {percent1:.2f}%")
    print(f"Contribution of the second triangle: {percent2:.2f}%")
