class Node:
  def __init__(self, key):
    self.key = key
    self.leftChild = None
    self.rightChild = None

class BinarySearchTree:
  def __init__(self):
    self.root = None
    self.size = 0

  def insert(self, item):
    self.size += 1
    if(self.root is None):
      self.root = Node(item)
    else:
      self._insert(self.root, item)

  def _insert(self, currNode, item):
    if(item < currNode.key):
      if(currNode.leftChild is None):
        currNode.leftChild = Node(item)
      else:
        self._insert(currNode.leftChild, item)
    else:
      if(currNode.rightChild is None):
        currNode.rightChild = Node(item)
      else:
        self._insert(currNode.rightChild, item)

  def preorderTraversal(self, currNode = None):
    if(currNode is None):
      currNode = self.root
    print(currNode.key)
    if(currNode.leftChild):
      self.preorderTraversal(currNode.leftChild)
    if(currNode.rightChild):
      self.preorderTraversal(currNode.rightChild)

  def __repr__(self):
    self.preorderTraversal()
    


bst = BinarySearchTree()

for item in [20, 10, 30, 12, 8, 11, 16]:
  bst.insert(item)

print("size is {}".format(bst.size))

print(bst)

