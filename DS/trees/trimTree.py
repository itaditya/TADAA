def trimBST(tree, minVal, maxVal):
  if(not tree):
    return

  tree.leftChild = trimBST(tree.leftChild, minVal, maxVal)
  tree.rightChild = trimBST(tree.rightChild, minVal, maxVal)

  if(minVal <= tree.key <= maxVal):
    return tree
  if(tree.key < minVal):
    return tree.rightChild
  if(tree.key > maxVal):
    return tree.leftChild

from binarySearchTree1 import BinarySearchTree

bst = BinarySearchTree(20)

for item in [10, 30, 14, 8, 16, 32, 18, 12, 13, 25]:
  bst.insert(item)

bst.preorderTraversal()

trimmedTree = trimBST(bst, 12, 30)

print('After trimming')
trimmedTree.preorderTraversal()

