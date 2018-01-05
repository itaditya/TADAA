from adjList import Graph

"""
from FOOL to SAGE and changing only one letter at a time

Sol : Build a graph in which each vertex is a word and if two nodes differ in only one char then connect them. Then find the shortest path
"""

perm = ["_OOL", "F_OL", "FO_L", "FOO_"]
letters = ["F", "O", "L", "S", "A", "G", "E"]

words = {}


g = Graph()

for p in perm:
  words[p] = []
  for l in letters:
    words[p].append(p.replace("_", l))

# print(words)

for p in perm:
  w = words[p]
  w_len = len(w)
  for i in w:
    for j in w:
      if(not(i == j)):
        g.addEdge(i, j)

for vertex in g:
  print(vertex)

