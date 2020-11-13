from UnorderedList import UnorderedList, Node

ul = UnorderedList()
ul.add(3)
ul.add(34)
ul.add(53)
ul.add(2)
ul.insert(44, 77)
ul.remove(34)
ul.append(1)
ul.display()
print(ul.pop(1))
ul.display()
print(ul.index(2))
print(ul.length())
print(ul.search(77))

