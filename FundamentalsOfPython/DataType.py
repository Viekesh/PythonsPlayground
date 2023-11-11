# You can get the data type of any object by using the type() function:

x = 5
print(type(x))

# In Python, the data type is set when you assign a value to a variable:
a = "Hello Python"
print(type(a))

b = 20.5
print(type(b))

c = 1j
print(type(c))

d = ["apple", "banan", "cherry"]
print(type(d))

e = ("pineapple", "kiwi", "orange")
print(type(e))

f = range(3)
print(type(f))

g = {
    "name": "John",
    "age": 30
}
print(type(g))

h = {"apple", "banana", "cherry"}
print(type(h))

i = frozenset({"guava", "grapes", "strawberry"})
print(type(i))

j = True
print(type(j))

k = b"Hello"
print(type(b))

l = bytearray(5)
print(type(l))

m = memoryview(bytes(5))
print(type(m))

n = None
print(type(n))


mestery = 734_529.678
# Even though the underscore is there to make the large number more readable, because there is a decimal
# point it is still a Float. If you printed the number in your code, it would be stripped down to 734529.678


# Type Checking And Type Conversion
num_of_char = len(input("What is your name? : "))

new_num_char = str(num_of_char)
# print(type(num_of_char))
print("Your name has " + new_num_char + " number of characters")


# Mathematical calculations followed in python language using PEMDAS sequence
# PEMDAS :

# Parenthesis("()")
# Exponents(**)
# Multiplication(*)
# Division(/)
# Addition(+)
# Subtraction(-)

# Sometimes multiplication (*), division (/) and addition (+), subtraction (-) have equal importance
print("PEMDAS :", 3 * 3 + 3 / 3 - 3)

# Here answer is 7.0 because mul, div and add, sub have equal importance, and python executes the statements
# using from top to down and left to right approach.

# Code Challenge 1: Change the above code to get the output from 7.0 to 3.0
print("Code Challenge :", 3 * (3 + 3) / 3 - 3)


# BMI calculator:

def calculate_bmi(weight, height):
    # calculate the BMI using the formula weight(kg) / (height(m) ** 2)
    bmi = weight / (height ** 2)

    # Interprete the BMI and print the result
    if bmi < 18.5:
        print("You are underweight.")
    elif 18.5 <= 24.9:
        print("You have a healthy weight.")
    elif 25 <= bmi <= 29.9:
        print("You are overweight.")
    else:
        print("You are obese.")

    return bmi


# get the users weight in kg
weight = float(input("Enter your weight in kg : "))
height = float(input("Enter your height in meter : "))

bmi = calculate_bmi(weight, height)
print("Your BMI is : ", bmi)
