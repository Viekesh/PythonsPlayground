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
