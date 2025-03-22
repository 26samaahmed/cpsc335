# Define the DFS function using recursion
def dfs(graph, node, visited=None):
  if visited is None:
      visited = set()

  # If the current node has not been visited yet
  if node not in visited:
      print(node) # Print the node (you can also store it in a list if needed)
      visited.add(node) # Mark the node as visited

      #Recursively visit each unvisited neighbor
      for neighbor in graph.get(node, []):
          dfs(graph, neighbor, visited) # Recursive DFS call for the neighbor


if __name__ == "__main__":
    # Initialize an empty graph using a dictionary
    graph = {}

    # Ask user how many connections (edges) in the graph
    print("Enter number of connections in the graph (edges):")
    edges = int(input())
    print("Enter each connection in the format: node1 node2")
    print("This will assume the graph is undirected (2-way connections)")

    # Read edges and populate the graph
    for _ in range(edges):
        u, v = input().split() # Read two connected nodes

        # Add edge from u -> v
        if u not in graph:
            graph[u] = [] # Initialize adjacency list for u
        graph[u].append(v)

        # Add edge from v -> u 
        if v not in graph:
            graph[v] = []
        graph[v].append(u) # Initialize adjacency list for v

    # Ask user for the starting node for DFS traversal
    print("Enter the starting node for DFS traversal:")
    start_node = input()
    print("\nDFS Traversal Order:")
    dfs(graph, start_node) # Call DFS function
    print('\n')
