Prim's Algorithm - Cost Efficient network design

Real world scenario - A company wants to connect all its office buildings with internet cables using minimum total cable cost. This forms a Minimum spanning tree (MST) - a subset of edges connecting all nodes without cycles and with minimum total edge weight

Key Idea:

1. Start from any node
2. Always connect the nearest unvisited node using the smallest edge
3. Avoid forming cycles

---

Kruskal Algorithm - Building Road Systems

Real world scenarion - A city planner wants to build roads connecting towns at the lowest total cost. The roads must form a connected map but avoid circular paths (no town should be visited twice in a single loop).

Key Idea:

1. Sort all edges by weight
2. Add the smallest edge that doesn't form a cycle (Union-Find/Disjoint Set to detect cycles)
3. Stop when all vertices are connected
