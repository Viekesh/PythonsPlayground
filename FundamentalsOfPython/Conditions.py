print("Welcome to the rollercoster")

height = int(input("What is your height in cm? :"))

if height > 120:
    print("You can ride on the rollercoster")
    age = int(input("Enter your age:"))
    if age < 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12")
else:
    print("Sorry, you have to grow taller before you can ride.")


# which number do you want ot check?

number = int(input("Enter the number :"))

if number % 2 == 0:
    print("This is a even number")
else:
    print("This is an odd number.")
