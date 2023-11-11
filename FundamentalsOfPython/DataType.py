# You can get the data type of any object by using the type() function:

x = 5
print(type(x))

# In Python, the data type is set when you assign a value to a variable:
a = "Hello Python"
print(type(a))

b = 20.5
print(type(b))

c = 1j
print(type(c))

d = ["apple", "banan", "cherry"]
print(type(d))

e = ("pineapple", "kiwi", "orange")
print(type(e))

f = range(3)
print(type(f))

g = {
    "name": "John",
    "age": 30
}
print(type(g))

h = {"apple", "banana", "cherry"}
print(type(h))

i = frozenset({"guava", "grapes", "strawberry"})
print(type(i))

j = True
print(type(j))

k = b"Hello"
print(type(b))

l = bytearray(5)
print(type(l))

m = memoryview(bytes(5))
print(type(m))

n = None
print(type(n))
