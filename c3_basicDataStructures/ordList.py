from OrderedList import OrderedList, Node

ol = OrderedList()
ol.add(1)
ol.add(23)
print(ol.index(1))
print(ol.length())
ol.add(17)
ol.add(58)
ol.pop(0)
ol.display()