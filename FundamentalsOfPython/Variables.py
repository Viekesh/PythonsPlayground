# Variables are containers for storing data values.
# Python has no command for declaring a variable.
# A variable is created the moment you first assign a value to it.

x = 5
y = "John"
print(x, y)


# Variables do not need to be declared with any particular type, and can even change type after they have
# been set.

a = 5  # a is of type int
a = "String"  # now a is of type string
print(a)

# If you want to specify the data type of a variable, this can be done with casting.
d = str(3)
e = int(3)
f = float(3)

print(d)
print(e)
print(f)


# You can get the data type of a variable with the type() function.
print(type(d))

# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)
# A variable name cannot be any of the Python keywords.
# Variable names with more than one word can be difficult to read.
# There are several techniques you can use to make them more readable such as camel case in which each word,
# except the first, starts with a capital letter:

myVariableName = "John"

# Pascal Case
# Each word starts with a capital letter:

MyVariableName = "John"

# Snake Case
# Each word is separated by an underscore character:

my_variable_name = "John"


# Python allows you to assign values to multiple variables in one line:

aa, bb, cc = "Orange", "Banana", "Cherry"
print(aa)
print(bb)
print(cc)

# Make sure the number of variables matches the number of values, or else you will get an error or you can
# assign the same value to multiple variables in one line:


# If you have a collection of values in a list, tuple etc. Python allows you to extract the values into
# variables. This is called unpacking.

fruits = ["apple", "banana", "cherry"]
ax, by, cz = fruits
print(ax)
print(by)
print(cz)

# The Python print() function is often used to output variables.
# In the print() function, you output multiple variables, separated by a comma:
# You can also use the + operator to output multiple variables:

var1 = "Now "
var2 = "we can "
var3 = "learn Python"
print(var1 + var2 + var3)


x = "awesome"


def myfunc():
    x = "fantastic"
    print("Python is ", x)


myfunc()
print("Python is " + x)

# To change the value of a global variable inside a function, refer to the variable by using the global
# keyword:

x = "awesome"


def myfunc():
    global x
    x = "fantastic"


myfunc()

print("Python is " + x)
