# Finding reachable cities from a source (e.g. Trip Planner)
from collections import deque

def bfs(graph, start):
    visited = set() # Set to keep track of visited cities
    queue = deque([start]) # Queue for BSF stariting from the given city
    print("\nBFS Traversal Order:")
    while queue:
        city = queue.popleft() # Dequeue a city 
        if city not in visited:
            print(city, end=" ") # Print the visited city
            visited.add(city) # Mark the city as visited
            for neighbor in graph.get(city, []): # Traverse its neighbors
                if neighbor not in visited:
                    queue.append(neighbor)


if __name__ == "__main__":
    graph = {}
    print("Enter number of Connections:")
    edges = int(input())
    print("Enter each connection (City1 City2):")
    for _ in range(edges):
        u, v = input().split()
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u) # undirected
    print("Enter the starting city for BFS:")
    start_city = input()
    bfs(graph, start_city)
    print('\n')