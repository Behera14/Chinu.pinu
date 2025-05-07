from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)  # Undirected

    # -------------------------------
    # Recursive DFS Helper Function
    # -------------------------------
    def dfs_util(self, current, visited, end, path):
        visited.add(current)
        path.append(current)
        if current == end:
            return True
        for neighbor in sorted(self.graph[current]):
            if neighbor not in visited:
                if self.dfs_util(neighbor, visited, end, path):
                    return True
        path.pop()
        return False

    # -------------------------------
    # DFS Entry Function
    # -------------------------------
    def dfs(self, start, end):
        print("\nDepth First Search (DFS):")
        visited = set()
        path = []
        found = self.dfs_util(start, visited, end, path)
        if found:
            print(" -> ".join(path))
        else:
            print(f"No path found from {start} to {end} using DFS.")

    # -------------------------------
    # Recursive BFS Helper Function
    # -------------------------------
    def bfs_recursive(self, queue, visited, end):
        if not queue:
            print(f"No path found using BFS.")
            return
        path = queue.popleft()
        current = path[-1]
        if current == end:
            print(" -> ".join(path))
            return
        for neighbor in sorted(self.graph[current]):
            if neighbor not in visited:
                visited.add(neighbor)
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
        self.bfs_recursive(queue, visited, end)

    # -------------------------------
    # BFS Entry Function (calls recursive)
    # -------------------------------
    def bfs(self, start, end):
        print("\n Breadth First Search (BFS):")
        visited = set([start])
        queue = deque([[start]])
        self.bfs_recursive(queue, visited, end)


# ------------------------------------
#  MAIN PROGRAM
# ------------------------------------
if __name__ == "__main__":
    print(" DFS and BFS (Recursive) in Undirected Graph \n")

    g = Graph()
    num_edges = int(input("Enter number of edges: "))

    print("Enter edges (e.g., A B):")
    for i in range(num_edges):
        u, v = input(f"Edge {i+1}: ").strip().split()
        g.add_edge(u.upper(), v.upper())

    start = input("\nEnter START node (A-Z): ").strip().upper()
    end = input("Enter END node (A-Z): ").strip().upper()

    if start not in g.graph or end not in g.graph:
        print(" Invalid start or end node.")
    else:
        g.dfs(start, end)
        g.bfs(start, end)


#Enter number of edges: 5
#Edge 1: A B
#Edge 2: A C
#Edge 3: B D
#Edge 4: C E
#Edge 5: D E
#Enter START node (A-Z): A
#Enter END node (A-Z): E
'''🧠 Summary: DFS vs BFS (Same Graph)
Feature	DFS	BFS
Search Strategy:	Deep first	Level     (breadth) first
Traversal Path	:A → B → D → E   	A → C → E
Uses	:Stack (via recursion)	Queue (even in recursion)
Goal	:Find any path to E	    Find shortest path to E

DFS
A → B

A → C

B → D

C → E

A

🔍 Depth First Search (DFS)
What it does: Explores as deeply as possible from the starting node before backtracking.

How it works: Start at the node, visit it, and go deeper to its unvisited neighbors. If there’s no way forward, backtrack and try another path.

Data Structure: Uses recursion (or stack).

Example: For the graph:

mathematica
Copy
Edit
    A
   / \
  B   C
 /     \
D       E
DFS might visit: A → B → D → C → E.

🔍 Breadth First Search (BFS)
What it does: Explores level by level. It visits all neighbors at the current level before moving deeper.

How it works: Start at the node, visit all its neighbors, then move to the next level of neighbors.

Data Structure: Uses a queue.

Example: For the graph:

mathematica
Copy
Edit
    A
   / \
  B   C
 /     \
D       E
BFS might visit: A → B → C → D → E.

🔑 Key Differences:
DFS: Deep first, uses recursion, backtracks when needed.

BFS: Wide first, uses a queue, explores level by level.'''