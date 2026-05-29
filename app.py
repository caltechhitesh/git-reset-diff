

# Student Marks Calculator

student_name = "Rahul"

maths = 85
science = 90
english = 78

total = maths + science + english
average = total / 3

print("Student Name:", student_name)
print("Maths Marks:", maths)
print("Science Marks:", science)
print("English Marks:", english)

print("Total Marks:", total)
print("Average Marks:", average)

# Result Check
if average >= 40:
    print("Result: Pass")
else:
    print("Result: Fail")