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
"""
Enter number of edges: 7
Enter edges (e.g., A B):
Edge 1: A B
Edge 2: A C
Edge 3: B D
Edge 4: C E
Edge 5: D F
Edge 6: E F
Edge 7: F G

Enter START node (A-Z): A
Enter END node (A-Z): G


      A
     / \
    B   C
    |    \
    D     E
     \   /
       F
        \
         G


Depth First Search (DFS):
A -> B -> D -> F -> G

Breadth First Search (BFS):
A -> C -> E -> F -> G


🔑 Key Differences:
DFS: Deep first, uses recursion, backtracks when needed.

BFS: Wide first, uses a queue, explores level by level.'''

A graph is a collection of nodes (vertices) and edges. In this case, it's an undirected graph (edges go both ways).

DFS (Depth First Search) explores as far as possible down one path before backtracking. It uses recursion and a visited set.

BFS (Breadth First Search) explores all neighbors at the current depth before moving to the next level. It uses a queue and level-wise expansion.

In the code:

dfs_util() is the recursive helper for DFS.

bfs_recursive() performs BFS using a queue recursively.


🔁 Stack
LIFO = Last In, First Out

Like a pile of books — last added is first removed

Used in DFS, backtracking, undo

🔁 Queue
FIFO = First In, First Out

Like a line at a shop — first in line goes first

Used in BFS, task scheduling

"""