def bubble_sort(data):
    """
    Sorts a list of data using bubble sort algorithm.

    Args:
        data: A list of sortable elements.

    Returns:
        A new list with the elements sorted in ascending order.
    """

    n = len(data)
    for i in range(n - 1):
        swapped = False
        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True
        if not swapped:
            break

    return data


# Unsorted list
unsorted_data = [5, 1, 4, 2, 8]

# Sort the list using bubble sort
sorted_data = bubble_sort(unsorted_data)

# Print the sorted list
print("Sorted list:", sorted_data)
