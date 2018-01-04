class BinaryTree(object):

  def __init__(self, rootNode):
    self.key = rootNode
    self.leftChild = None
    self.rightChild = None

  def insertLeft(self, newNode):
    if(self.leftChild is None):
      self.leftChild = BinaryTree(newNode)
    else:
      t = BinaryTree(newNode)
      t.leftChild = self.leftChild
      self.leftChild = t

  def insertRight(self, newNode):
    if(self.rightChild is None):
      self.rightChild = BinaryTree(newNode)
    else:
      t = BinaryTree(newNode)
      t.rightChild = self.rightChild
      self.rightChild = t

  def getRootVal(self):
    return self.key

  def setRootVal(self, newVal):
    self.key = newVal

  def preorderTraversal(self):
    print(self.key)
    if(self.leftChild):
      self.leftChild.preorderTraversal()
    if(self.rightChild):
      self.rightChild.preorderTraversal()

  def inorderTraversal(self):
    if(self.leftChild):
      self.leftChild.inorderTraversal()
    print(self.key)
    if(self.rightChild):
      self.rightChild.inorderTraversal()

  def postorderTraversal(self):
    if(self.leftChild):
      self.leftChild.postorderTraversal()
    if(self.rightChild):
      self.rightChild.postorderTraversal()
    print(self.key)

    

if(__name__ == '__main__'):
  r = BinaryTree(20)
  r.insertLeft(10)
  r.insertRight(30)
  r.leftChild.insertLeft(8)
  r.leftChild.insertRight(12)
  r.leftChild.rightChild.insertLeft(11)
  r.leftChild.rightChild.insertRight(16)

  print("Preorder : ")
  r.preorderTraversal()
  print("Inorder : ")
  r.inorderTraversal()
  print("Postorder : ")
  r.postorderTraversal()

"""
Tree --->
                                        20
                              10                30
                        8         12
                                11  16
"""
# Preorder: PLR
# Inorder: LPR
# Postorder: LRP
