class BinaryHeap(object):
  #minheap
  def __init__(self):
    self.heapList = [0]
    self.size = 0

  def percUp(self, i):
    if(i > 1):
      parent = i // 2
      if(self.heapList[parent] > self.heapList[i]):
        self.heapList[parent], self.heapList[i] = self.heapList[i], self.heapList[parent]
        self.percUp(parent)

  def insert(self, item):
    self.heapList.append(item)
    self.size += 1
    self.percUp(self.size)

  def minChild(self, i):
    leftChild = 2 * i
    rightChild = leftChild + 1

    mc = rightChild

    if(rightChild > self.size):
      mc = leftChild
    else:
      if(self.heapList[leftChild] < self.heapList[rightChild]):
        mc = leftChild
        
    return mc

  
  def percDown(self, i):
    leftChild = 2 * i
    rightChild = leftChild + 1

    if(leftChild > self.size):
      return

    mc = self.minChild(i)

    if(self.heapList[mc] < self.heapList[i]):
      self.heapList[mc], self.heapList[i] = self.heapList[i], self.heapList[mc]
      self.percDown(mc)


  def delMin(self):
    root = self.heapList[1]
    self.heapList[1] = self.heapList[self.size]
    self.size -= 1
    self.heapList.pop()
    self.percDown(1)


b1 = BinaryHeap()
b2 = BinaryHeap()
for item in [5, 9, 11, 14, 18, 19, 21, 33, 17, 27]:
  b1.insert(item)
  b2.insert(item)

print(b1.heapList)
b1.insert(7)
print(b1.heapList)
b1.insert(3)
print(b1.heapList)

print(b2.heapList)
b2.delMin()
print(b2.heapList)

