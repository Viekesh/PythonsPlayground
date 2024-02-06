# height = int(input("Enter your height in cm :"))
# weight = int(input("Enter your weight in kg :"))

# BMI = weight / (height * height)

# print("Your BMI is ", BMI)

# if BMI < 18.5:
#     print("Your BMI is {BMI} you are underweight.")
# elif BMI < 25:
#     print("Your BMI is " BMI "your weight is normal.")
# elif BMI < 30:
#     print("Your BMI is " BMI "you are slightly underweight.")
# elif BMI < 35:
#     print("Your BMI is" BMI " you are obese.")
# else:
#     print("Your BMI is " BMI "you are clinically obese.")


# Calculate BMI and print appropriate message

# Replace with actual height in cm
height = int(input("Enter Your height in cm :"))
# Replace with actual weight in kg
weight = int(input("Enter your weight in kg :"))

bmi = weight / (height / 100)**2

if bmi < 18.5:
    print("you are underweight.")
elif bmi >= 25 and bmi < 30:
    print("You are overweight.")
elif bmi >= 30:
    print("You are clinically obese.")
else:
    print("You are within the healthy range.")
