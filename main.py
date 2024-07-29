# Import all modules and functions from questions.py and print all the outputs to the console.

# Answer
from questions import qn1, qn2, qn3, qn4, qn5, qn6, qn7, qn8, qn9, qn10

# Question 1
print("Question 1")
print(qn1.qnListSum)
print(qn1.qnListMultiply)
print(qn1.qnListSmallestNumber)
print(qn1.qnListLargestNumber)
print()

# Question 2
print("Question 2")
print(qn2.similarityList)
print()

# Question 3
print("Question 3")
print("Pattern 1:")
for line in qn3.patternListA:
    print(line[0], end="")
    for char, tab in line[1]:
        print(char, end=tab)
    print(line[2], end="")
print()
print("Pattern 2:")
for line in qn3.patternListB:
    print(line)

# Question 4
print("Question 4")
print(qn4.clrDictionary)
print()

# Question 5
print("Question 5")
print("Subpart A: range(1, 50)")
print(qn5.evenNumListA)
print()
print("Subpart B: range(1, 100)")
print(qn5.evenNumListB)
print()

# # Question 6
# print("Question 6")
# qn6.processFourDigitNumber()
# print()

# # Question 7
# print("Question 7")
# qn7.find_triangle_areas_and_contributions()
# print()

# Question 8
print("Question 8")
qn8.print_people_info(qn8.people)
print()

# Question 9
print("Question 9")
qn9.extract_last_characters(qn9.input_tuple)
print()

# # Question 10
# print("Question 10")
# qn10.get_days_in_month_by_input()
# print()
