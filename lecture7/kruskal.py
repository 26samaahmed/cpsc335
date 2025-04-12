def find(parent, x):
  if parent[x] != x:
    parent[x] = find(parent, parent[x])
  return parent[x]


def union(parent, rank, x, y):
  rootX = find(parent, x)
  rootY = find(parent, y)
  if rootX != rootY:
    if rank[rootX] < rank[rootY]:
      parent[rootX] = rootY
    elif rank[rootX] > rank[rootY]:
      parent[rootY] = rootX
    else:
      parent[rootY] = rootX
      rank[rootX] += 1

def kruskal(n, edges):
  edges.sort(key=lambda x: x[2])  # Sort edges based on weight
  parent = [i for i in range(n)]
  rank = [0] * n
  mst_cost = 0
  mst_edges = []

  for u, v, weight in edges:
    if find(parent, u) != find(parent, v):
      union(parent, rank, u, v)
      mst_cost += weight
      mst_edges.append((u, v, weight))
  return mst_cost, mst_edges


n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))
edges = []

for _ in range(e):
    u, v, w = map(int, input("Enter edge (u v weight): ").split())
    edges.append((u, v, w))

cost, mst_edges = kruskal(n, edges)
print("Minimum Cost to Connect all nodes: ", cost)
print("Edges in the MST: ", mst_edges)