def create_magic_square(n):
    square = [[0 for x in range(n)] for y in range(n)]

    i = n // 2  # Start in the middle of the top row
    j = n - 1  # Start in the rightmost column
    num = 1

    while num <= n * n:
        # Check if wrapping is needed
        if i == -1 and j == n:  # Bottom right corner
            i = 0
            j = n - 2  # Wrap to the second last column
        elif i == -1:  # Wrap to bottom row
            i = n - 1
        elif j == n:  # Wrap to leftmost column
            j = 0

        # Place the number and move diagonally
        square[i][j] = num
        num += 1
        i -= 1
        j += 1

    return square


# Create a 3x3 magic square
magic_square = create_magic_square(3)

# Print the magic square
for i in range(3):
    for j in range(3):
        print(magic_square[i][j], end=" ")
    print()
