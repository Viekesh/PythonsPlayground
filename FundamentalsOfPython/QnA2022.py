# Write a code to find the largest of three numbers.

print("find the largest of three numbers using conditional statement")

# This line prompts the user to enter a number and stores it in the variable num1. The int function converts the
# user input to an integer.
num1 = int(input("Enter first number :"))

# This line prompts the user to enter another number and stores it in the variable num2. The int function converts
# the user input to an integer.
num2 = int(input("Enter second number :"))

# This line prompts the user to enter another number and stores it in the variable num3. The int function converts
# the user input to an integer.
num3 = int(input("Enter third number"))

# This line starts an if statement that checks if num1 is greater than both num2 and num3.
if num1 > num2 and num1 > num3:

    # This line prints the message "The first number you entered is the largest of the other two numbers.." to the
    # console if the condition in the if statement is true.
    print("The first number you entered is the largest of the other two numbers.")

# This line starts an elif statement that checks if num2 is greater than both num1 and num3.
elif num2 > num1 and num2 > num3:

    # This line prints the message "The second number you entered is the largest of the other two numbers.." to
    # the console if the condition in the elif statement is true.
    print("The second number you entered is the largest of the other two numbers.")

# This line starts an else statement that is executed if neither of the conditions in the if or elif statements
# are true.
else:

    # This line prints the message "The third number you entered is the largest of the other two numbers." to the # console if the condition in the else statement is true.
    print("The third number you entered is the largest of the other two numbers.")


#
#
#


# What is the difference between for loop and while loop?

# "for loop" is used when the exact number of iteration is known beforehand.
# "while loop" is used when the exact number of iteration is not known beforehand or when the loop should continue
# as long as a certain condition is meet.

# In "for loop" initialisation is explicitly stated
# In "while loop" initialisation is not required

# "for loop" is more readable because the number of iteration is clear
#  "while loop" is more concise because condition is the focus.

# "for loop" is faster than while loop due to known of iteration.
# "while loop" is slower than for loop due to potential for infinite loop.

# syntax "for loop";

# for(initialisation; condition; increment/decrement) {
#     code to be executed
# }
# initialisation sets up the counter variable before the loop begins.
# condition is a boolean expression that determines whether the loop continue.
# increment/decrement updates the counter variable after each iteration.

# while(condition) {
    # code to be executed
    # update the condition as needed
# }
# condition is a boolean expression that determines whether the loop continue. The loop is continue as long as the
# condition is true.
# The loop code should update the condition within the loop to ensure it eventually becomes false and exits the
# loop. Otherwise, it will become an infinite loop.

# for loop example
numbers = [1, 2, 3, 4, 5]
# this line defines a list named "numbers" containing five integers.

for number in numbers:  # This is the "for" loop header. It iterates through each element in the "numbers" list
    print("for loop : ", number)


i = 1
while i < 10:
    print("while loop : ", i)
    i += 1

#
#
#

# write a code which iterates from numbers 1 to 100 display "fizz" if the number is divisible by "a" but not "b",
# displays "buzz" if the number is divisible by b but not a, and displays "fizzbuzz" if the number is divisible by
# both "a" and "b". "a" and "b" are the inputs taken from the user.

a = int(input("Enter value for a : "))
b = int(input("Enter value for b : "))

for i in range(1, 101):
    if i % a == 0 and i % b != 0:
        print("fizz")
    elif i % a != 0 and i % b == 0:
        print("buzz")
    elif i % a == 0 and i % b == 0:
        print("fizzbuzz")
    else:
        print(i)
