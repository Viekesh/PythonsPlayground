def average_of_n_integers():
    """Gets N integers from the user, stores them in a list, and calculates the average."""

    num_integers = int(input("Enter the number of integers (N): "))
    integers_list = []  # Create an empty list to store integers

    for i in range(num_integers):
        integer = int(input(f"Enter integer {i + 1}: "))
        integers_list.append(integer)  # Add integer to the list

    total = sum(integers_list)  # Calculate the sum of integers
    average = total / num_integers  # Calculate the average

    print("The average of the entered integers is:", average)


average_of_n_integers()  # Call the function to execute the program
