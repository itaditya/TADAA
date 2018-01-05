class Vertex:
  def __init__(self, key):
    self.key = key
    self.neighbors = {}

  def addNeighbor(self, nbr, wt = 0):
    self.neighbors[nbr.key] = wt

  def getNeighbors(self):
    return self.neighbors.keys()

  def __str__(self):
    return "{} connected to {}".format(str(self.key), str(list(self.getNeighbors())))

class Graph:
  def __init__(self):
    self.vertices = {}
    self.numVertices = 0

  def addVertex(self, key):
    v = Vertex(key)
    self.vertices[key] = v
    self.numVertices += 1
    return v

  def getVertex(self, key):
    if(key in self.vertices):
      return self.vertices[key]
    return None

  def addEdge(self, src, dest, wt = 0):
    if(src not in self.vertices):
      self.addVertex(src)
    if(dest not in self.vertices):
      self.addVertex(dest)

    self.vertices[src].addNeighbor(self.vertices[dest], wt)

  def getVertices(self):
    return self.vertices.keys()

  def __iter__(self):
    return iter(self.vertices.values())

  def __contains__(self):
    return n in self.vertices


if(__name__ == '__main__'):
  v0 = Vertex(1)
  v1 = Vertex(2)
  v2 = Vertex(3)
  v3 = Vertex(4)

  v1.addNeighbor(v0,5)
  v3.addNeighbor(v2,3)
  v1.addNeighbor(v2,7)

  print(v1)
  print(v1.getNeighbors())

  g = Graph()
  for i in range(6):
    g.addVertex(i)
  g.addEdge(0, 1, 7)

  for vertex in g:
    print(vertex)
    print(vertex.getNeighbors(), "\n")

  
