from BinarySearchTree import BST
from Node import Node

tree = BST()
tree.setRoot(5)
tree.insert(3)
tree.insert(8)
tree.insert(4)
tree.insert(6)
tree.insert(2)
tree.insert(7)
print(tree.getPreOrder())
print(tree.getInOrder())
print(tree.getPostOrder())
