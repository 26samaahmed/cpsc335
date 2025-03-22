# Modeling city connections in a transportation network to understand graphs
class Graph:
  def __init__(self):
    self.graph = {}

  def add_edge(self, u, v):
    if u not in self.graph:
      self.graph[u] = []
    if v not in self.graph:
      self.graph[v] = []
    self.graph[u].append(v)
    self.graph[v].append(u)  # Assuming undirected graph

  def display(self):
    print("\nGraph Representation (Adjecency List):")
    for city in self.graph:
      print(f"{city} --> {self.graph[city]}")

if __name__ == "__main__":
  g = Graph()
  print("Enter number of connections (edges):")
  edges = int(input())
  print("Now enter each connection format: City1 City2")
  for _ in range(edges):
    u, v = input().split()
    g.add_edge(u, v)
  g.display()