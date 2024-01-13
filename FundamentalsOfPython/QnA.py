# que 1: Write a code to find a largest of three numbers.

# using the built in max function:

print("Write a code to find the largest of three numbers")
num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))
num3 = int(input("Enter the three number : "))

largest = max(num1, num2, num3)

print("The largest number is ", largest)


# using conditional statement
print("find a largest of three numbers using conditional statement")
num4 = int(input("Enter the first number"))
num5 = int(input("Enter any digit of number"))
num6 = int(input("Enter the third number"))

if num4 > num5 and num4 > num6:
    print("largest number is : ", num4)
elif num5 > num4 and num5 > num6:
    print("largest number is : ", num5)
else:
    print("largest number is : ", num6)
# if num4 > num5 and num4 > num6:
#     print("largest number is:", num4)
# elif num5 > num4 and num5 > num6:
#     print("largest number is : ", num5)
# else:
#     print("largest number is : ", num6)


first_num = int(input("Enter any number : "))
sec_num = int(input("Enter any number : "))
third_num = int(input("Enter any number : "))


if first_num > sec_num and first_num > third_num:
    print("The largest number is : ", first_num)
elif sec_num > first_num and sec_num > third_num:
    print("The largest number is : ", sec_num)
else:
    print("The largest num is : ", third_num)


# que 2: difference between for loop and while loop. write the syntax of for and while loop.

# "for loop" is used when the exact number of iteration is known beforehand.
# "while loop" is used when the exact number of iteration is not known beforehand or when the loop should continue # as long as a certain condition is meet.

# In "for loop" initialisation is explicitly stated
# In "while loop" initialisation is not required

# "for loop" is more readable because the number of iteration is clear
#  "while loop" is more concise because condition is the focus.

# "for loop" is faster than while loop due to known of iteration.
#  "while loop" is slower than for loop due to potential for infinite loop.

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


# que 3: write a code which iterates from numbers 1 to 100 display "fizz" if the number is divisible by "a" but
# not "b", displays "buzz" if the number is divisible by b but not a, and displays "fizzbuzz" if the number is
# divisible by both "a" and "b". "a" and "b" are the inputs taken from the user.
