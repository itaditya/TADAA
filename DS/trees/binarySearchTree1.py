class BinarySearchTree:
  def __init__(self, rootNode):
    self.key = rootNode
    self.leftChild = None
    self.rightChild = None
    self.parent = None

  def isLeftChild(self):
    return self.parent.leftChild == self

  def isRightChild(self):
    return self.parent.rightChild == self

  def insert(self, item):
    if(item < self.key):
      if(self.leftChild is None):
        self.leftChild = BinarySearchTree(item)
        self.leftChild.parent = self
      else:
        self.leftChild.insert(item)
    else:
      if(self.rightChild is None):
        self.rightChild = BinarySearchTree(item)
        self.rightChild.parent = self
      else:
        self.rightChild.insert(item)


  def delete(self, item):
    itemExists, itemInstance = self.contains(item)
    if(itemExists):
      if(itemInstance.leftChild is None and itemInstance.rightChild is None):
        # leaf node
        if(itemInstance.isLeftChild()):
          itemInstance.parent.leftChild = None
        else:
          itemInstance.parent.rightChild = None

      elif(itemInstance.rightChild is None):
        # only left child
        if(itemInstance.parent is None):
          itemInstance.leftChild.parent = None
        else:
          if(itemInstance.isLeftChild()):
            itemInstance.parent.leftChild = itemInstance.leftChild
          else:
            itemInstance.parent.rightChild = itemInstance.leftChild
          itemInstance.leftChild.parent = itemInstance.parent

      elif(itemInstance.leftChild is None):
        # only right child
        if(itemInstance.parent is None):
          itemInstance.rightChild.parent = None
        else:
          if(itemInstance.parent.leftChild == itemInstance):
            #itemInstance is left child of parent
            itemInstance.parent.leftChild = itemInstance.rightChild
          else:
            itemInstance.parent.rightChild = itemInstance.rightChild
          itemInstance.rightChild.parent = itemInstance.parent

      else:
        # two children
        successor = itemInstance.findSuccessor()
        # successor is either leaf or has only right child
        # print("successor", successor)
        self.delete(successor.key)
        itemInstance.key = successor.key



  def contains(self, item):
    if(item == self.key):
      return (True, self)
    elif(item < self.key):
      if(self.leftChild is None):
        return (False)
      else:
        return self.leftChild.contains(item)
    else:
      if(self.rightChild is None):
        return (False)
      else:
        return self.rightChild.contains(item)

  def findMin(self):
    if(self.leftChild is None):
      return self
    return self.leftChild.findMin()

  def findSuccessor(self):
    if(not(self.rightChild is None)):
      succ = self.rightChild.findMin()
    return succ

  def validateBST(self):
    if(self.leftChild):
      if(self.leftChild.key < self.key):
        return self.leftChild.validateBST()
      else:
        return False
    if(self.rightChild):
      if(self.rightChild.key >= self.key):
        return self.rightChild.validateBST()
      else:
        return False
    return True


  def preorderTraversal(self):
    print(self.key)
    if(self.leftChild):
      self.leftChild.preorderTraversal()
    if(self.rightChild):
      self.rightChild.preorderTraversal()

  def __str__(self):
    return str(self.key)
    

if(__name__ == '__main__'):
  bst = BinarySearchTree(20)

  for item in [10, 30, 14, 8, 16, 32, 18, 12, 13, 25]:
    bst.insert(item)

  bst.preorderTraversal()

  has7 = bst.contains(7)
  print(has7)
  has13, has13Instance = bst.contains(13)
  print(has13, has13Instance)


  print("delete leaf node")
  bst.delete(8)
  bst.preorderTraversal()

  print("delete nodes with one child")
  bst.delete(16)
  bst.delete(12)
  bst.preorderTraversal()

  print("delete nodes with two children")
  bst.delete(14)
  bst.preorderTraversal()

  print("delete root")
  bst.delete(20)
  bst.preorderTraversal()

  print("Validate bst", bst.validateBST())
  from binaryTree import BinaryTree
  r = BinaryTree(20)
  r.insertLeft(10)
  r.insertRight(30)
  r.leftChild.insertLeft(12)
  r.leftChild.insertRight(8)
  BinaryTree.validateBST = BinarySearchTree.validateBST
  print("Validate r", r.validateBST())




"""
Tree --->
                                        20
                              10                30
                        8         14        25      32
                               12    16
                                13     18
"""


