# This advanced example demonstrates unpacking data, building a dictionary dynamically, and using loop variables
# effectively.

# We initialize an empty dictionary named students to store student information.
students = {}

# We define a list named data containing tuples of student names and their corresponding grades.
studentData = [("Alice", 90), ("Bob", 91), ("John", 94)]

# This is an advanced for loop that unpacks each tuple in the data list.
# name and grade become separate loop variables holding the values from each tuple during each iteration.
for name, grades in studentData:

    # We add a new key-value pair to the students dictionary.
    # The key is the current name from the loop, and the value is the corresponding grade.
    students[name] = grades

# This line prints the final students dictionary containing all student names and their grades.
print(students)
