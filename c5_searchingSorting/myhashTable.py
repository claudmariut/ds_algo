from HashTable import HashTable

h = HashTable()
h[54] = "cat"
h[26] = "dog"
h[93] = "lion"
h[17] = "tiger"
h[77] = "bird"
h[31] = "cow"
h[44] = "goat"
h[55] = "pig"
h[20] = "chicken"

del h[55]

print(h.keys)
print(h.data)
print(len(h))
print("goat" in h)


