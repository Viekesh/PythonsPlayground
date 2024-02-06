def factorial(n):
    """Calculates the factorial of a non-negative integer using recursion.

    Args:
      n: The non-negative integer for which to calculate the factorial.

    Returns:
      The factorial of n.

    Raises:
      ValueError: If n is negative.
    """

    if n < 0:
        raise ValueError("n must be non-negative")
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)  # Recursive call


# Get input number from the user
num = int(input("Enter a non-negative number: "))

# Calculate and print the factorial
result = factorial(num)
print(f"The factorial of {num} is: {result}")
