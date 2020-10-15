myList = [1, 2, 3, 4]
# The result of a repetition operator is a repetition of references to the data
A = [myList] * 3
print(A)

myList[2] = 45
print(A)  # This looks to he reference list to return a result.

myList2 = [1, 2, 3]
B = myList2 + myList2
print(B)

myList2[1] = 24
print(B)  # Same result as previous. Is not taken from reference.

# Work with items in list methods.
listMethods = [1, 2, 3, 4, 2, 2]
print(listMethods.index(2))  # First occurrence.
print(listMethods.count(2))
print(listMethods.remove(2))  # First occurrence.

# List comprehensions.
myList3 = [x**2 for x in range(1, 11)]
print(myList3)

myList4 = [x*x for x in range(1, 11) if x % 2 != 0]
print(myList4)

myList5 = [ch.upper() for ch in "data structures" if ch not in "aeiou"]
print(myList5)
