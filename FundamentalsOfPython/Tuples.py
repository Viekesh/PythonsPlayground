# source: https://www.w3schools.com/python/python_tuples.asp



# Tuples:

# Tuples are used to store multiple items in a single variable.
# Tuple is one of 4 built-in data types in Python used to store
# collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
# A tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets.



# ex 1:

thisTuple = ("apple", "banana", "cherry")
print(thisTuple)









# Tuple Items
# Tuple items are ordered, unchangeable, and allow duplicate values.
# Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

# Ordered
# When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

# Unchangeable
# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

# Allow Duplicates
# Since tuples are indexed, they can have items with the same value:



# ex 2:

thisTuple2 = ("apple", "banana", "cherry", "apple", "banana")
print(thisTuple2)









# Tuple Length
# To determine how many items a tuple has, use the len() function:

# ex 3:

print(len(thisTuple))









# Tuple Items - Data Types
# Tuple items can be of any data type:

# ex 4:

tuple1 = ("apple", "banana", "mango")
tuple2 = (1, 2, 3, 4, 5)
tuple3 = (True, False)

print(tuple1, tuple2, tuple3)



# A tuple can contain different data types.

tuple4 = ("apple", 1, 2, 3, True, False)
print(tuple4)



