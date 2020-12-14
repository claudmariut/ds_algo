"""
We can create hash function for characer-based items such as strings.
Using ord() function to return ordinal values in ASCII Table for characters.
"""


def hash(astring, tablesize):
    sum = 0
    for char in astring:
        sum += ord(char)
    # returns hash value in the range of 0 - tablesize - 1
    return sum % tablesize


print(hash("cat", 11))

"""
This last approach works fine, but notice that for anagrams, the value returned
is the same. A possible way to solve this would be use the position value
as a weighting factor. See example bellow.
"""


def hash2(astring, tablesize):
    sum = 0
    for pos in range(len(astring)):
        # Multiply each char order by position + 1.
        sum += (pos + 1) * ord(astring[pos])
    return sum % tablesize


print(hash2("cat", 11))
