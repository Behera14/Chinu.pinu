import heapq
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v, weight):
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))  # undirected graph

    def dijkstra(self, start, end):
        print(f"\n Dijkstra's Algorithm: Evaluate All Paths from '{start}'\n")

        distances = {node: float('inf') for node in self.graph}
        predecessors = {node: None for node in self.graph}
        distances[start] = 0
        pq = [(0, start)]
        visited = set()

        while pq:
            current_dist, current_node = heapq.heappop(pq)
            if current_node in visited:
                continue
            visited.add(current_node)

            for neighbor, weight in self.graph[current_node]:
                new_dist = current_dist + weight
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    predecessors[neighbor] = current_node
                    heapq.heappush(pq, (new_dist, neighbor))

        #  Display all paths
        print(" All shortest distances and paths from:", start)
        for node in sorted(self.graph.keys()):
            if distances[node] == float('inf'):
                print(f" {node} is not reachable.")
            else:
                path = self.get_path(predecessors, node)
                print(f"🔹 To {node}: Distance = {distances[node]}, Path = {path}")

        # Final requested path
        if distances[end] == float('inf'):
            print(f"\n No path exists from {start} to {end}")
        else:
            path = self.get_path(predecessors, end)
            print(f"\n Final shortest path from {start} to {end}:")
            print(f" Path: {path}")
            print(f"Distance: {distances[end]}")

    def get_path(self, predecessors, end):
        path = []
        while end is not None:
            path.append(end)
            end = predecessors[end]
        return ' -> '.join(reversed(path))

# ------------------------------
#  Main Driver Code
# ------------------------------
if __name__ == "__main__":
    g = Graph()
    print(" Dijkstra's Algorithm - Evaluate All Paths + Final Shortest\n")
    num_edges = int(input("Enter number of edges: "))
    print("Enter edges as: <FROM> <TO> <WEIGHT> (Example: A B 4)")

    for i in range(num_edges):
        u, v, w = input(f"Edge {i+1}: ").split()
        g.add_edge(u.upper(), v.upper(), int(w))

    start_node = input("\nEnter the START node (A-Z): ").strip().upper()
    end_node = input("Enter the END node (A-Z): ").strip().upper()

    g.dijkstra(start_node, end_node)
""" What is Greedy Search Algorithm?
A Greedy Search Algorithm builds a solution by always choosing the option that looks most immediately promising, without worrying about the overall optimal solution.

It uses a priority queue to always expand the node with the lowest cost so far.

Dijkstra’s Algorithm is a classic greedy algorithm for shortest path finding in a weighted graph with non-negative edges.

✅ Why Dijkstra is Greedy:
At each step, it chooses the unvisited node with the smallest known distance from the start.

It assumes that by picking the nearest node, we’re always getting closer to the destination — that’s the greedy part!

📌 Your Code: Dijkstra’s Algorithm (Greedy Approach)
🔹 add_edge(u, v, weight):
Adds an undirected edge between nodes u and v with given weight.

🔹 dijkstra(start, end):
Initializes distances from start to all nodes as ∞ (infinity), except start = 0.

Uses a priority queue (min-heap) to always pick the node with the shortest known distance.

Updates neighbors’ distances if a shorter path is found.

Keeps track of predecessors to reconstruct paths later.

Prints shortest distances to all nodes, and specifically shows the shortest path from start to end.

🔹 get_path(predecessors, end):
Reconstructs the path from start to any node by backtracking using the predecessors.

✨ Example Use Case:
Input:
mathematica
Copy
Edit
Enter number of edges: 5
A B 1
B C 2
A C 4
C D 1
B D 5
START: A
END: D
Output:
mathematica
Copy
Edit
To D: Distance = 4, Path = A -> B -> C -> D
✔ Greedy nature: always expanded the nearest node first (A -> B, then B -> C, then C -> D).

📌 Summary:
Feature	Description
Type	Greedy Search
Algorithm	Dijkstra’s Algorithm
Goal	Find shortest path in a graph with non-negative weights
Key Structure	Priority Queue (Min-Heap)
Strategy	Always pick node with smallest current cost"""
