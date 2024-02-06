# write a code which iterates from numbers 1 to 100 display "fizz" if the number is divisible by "a" but not "b",
# displays "buzz" if the number is divisible by b but not a, and displays "fizzbuzz" if the number is divisible by
# both "a" and "b". "a" and "b" are the inputs taken from the user.

# line first and second assigns the user input to a variable a and b after converting it to an integer.
a = int(input("Enter value for a : "))
b = int(input("Enter value for b : "))

# This line iterates from 1 to 100 and assigns the current number to variable i in each iteration.
for i in range(1, 101):

    # This line checks if current number is divisible by a but not divisible by b, if the condition is true
    # the print function prints "fizz"
    if i % a == 0 and i % b != 0:
        print("fizz")

    # This line checks if the current number is not divisible by a but divisible by b, if the condition
    # is true the print function prints the "buzz"
    elif i % a != 0 and i % b == 0:
        print("buzz")

    # This line checks the current number is divisible by both a and b if the condition is true the
    # print function prints the "fizzbuzz"
    elif i % a == 0 and i % b == 0:
        print("fizzbuzz")

    # If all the condition remains false then the print function of else part print the current number.
    else:
        print(i)
