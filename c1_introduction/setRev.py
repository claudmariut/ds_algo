mySet = {False, 4.5, 3, 6, 'cat'}
print(False in mySet)

yourSet = {99, 3, 100}

# Returns a set with both elements from sets.
print(mySet | yourSet)
print(mySet.union(yourSet))

# Returns set with common elements.
print(mySet & yourSet)
print(mySet.intersection(yourSet))

# Returns set with all items from the first set not in the second.
print(mySet - yourSet)
print(mySet.difference(yourSet))

# Ask if all elements of the first set are in the second.
print(mySet <= yourSet)
print(mySet.issubset(yourSet))

# Removes arbitrary element. But we can user .remove(item) also.
mySet.pop()

