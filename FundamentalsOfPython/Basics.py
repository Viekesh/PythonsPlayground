print("Hello Python")


# Indentation refers to the spaces at the beginning of a code line.
# Python uses indentation to indicate a block of code.

if (5 > 2):
    print("Five is greater than 2")


# In Python, variables are created when you assign a value to it:
# Python has no command for declaring a variable.

x = 5
y = "Hello Python"
print(x, ",", y)


# Comments can be used to explain Python code.
# Comments can be used to make the code more readable.
# Comments can be used to prevent execution when testing code.
# Comments can be placed at the end of a line, and Python will ignore the rest of the line:
# To add a multiline comment you could insert a # for each line:
# Or, not quite as intended, you can use a multiline string.

"""
Since Python will ignore string literals that are not assigned to a variable, you can add a multiline string (triple quotes) in your code, and place your comment inside it:
"""
# As long as the string is not assigned to a variable, Python will read the code, but then ignore it, and
# you have made a multiline comment.
