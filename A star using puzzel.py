def accept(n):
    """Accepts the puzzle from the user"""
    puz = []
    for i in range(n):
        puz.append([val for val in input().split()])
    return puz

def print_board(board, n):
    for i in range(n):
        print()
        for j in range(n):
            print(board[i][j], end=' ')
    print()

def find_space(Current, n):
    """Find the position of blank space"""
    for i in range(n):
        for j in range(n):
            if Current[i][j] == '_':
                return i, j

def copy_current(Current):
    """Create a deep copy of the current state"""
    return [row[:] for row in Current]

def shuffle(Current, brow_pos, bcol_pos, move_x, move_y):
    """Move the blank space"""
    if 0 <= move_x < len(Current) and 0 <= move_y < len(Current):
        temp = copy_current(Current)
        temp[brow_pos][bcol_pos], temp[move_x][move_y] = temp[move_x][move_y], temp[brow_pos][bcol_pos]
        return temp
    else:
        return None

def g_score(Node):
    return Node[1]

def h_score(Current, Goal, n):
    """Misplaced tile heuristic"""
    hscore = 0
    for i in range(n):
        for j in range(n):
            if Current[i][j] != Goal[i][j] and Current[i][j] != '_':
                hscore += 1
    return hscore

def f_score(Node, Goal, n):
    """f(n) = g(n) + h(n)"""
    return g_score(Node) + h_score(Node[0], Goal, n)

def move_gen(Node, Goal, n):
    """Generate children of a node"""
    Current = Node[0]
    level = Node[1]
    row, col = find_space(Current, n)

    move_positions = [[row, col - 1], [row, col + 1], [row - 1, col], [row + 1, col]]
    children = []

    for move in move_positions:
        child_board = shuffle(Current, row, col, move[0], move[1])
        if child_board is not None:
            child_node = [child_board, level + 1, 0]
            child_node[2] = f_score(child_node, Goal, n)
            children.append(child_node)

    return children

def goal_test(Current, Goal, n):
    return h_score(Current, Goal, n) == 0

def sort_open_list(L):
    """Sort OPEN list based on f_score"""
    L.sort(key=lambda x: x[2])
    return L

def play_game(Start, Goal, n):
    """Main A* loop"""
    start_node = [Start, 0, 0]
    start_node[2] = f_score(start_node, Goal, n)

    OPEN = [start_node]
    CLOSED = []

    while OPEN:
        N = OPEN.pop(0)
        Current = N[0]
        CLOSED.append(N)

        print("\nCurrent configuration (Level", N[1], "):")
        print_board(Current, n)

        if goal_test(Current, Goal, n):
            print("\n Goal reached!!")
            print(" Total moves taken:", N[1])
            return

        children = move_gen(N, Goal, n)
        OPEN.extend(children)
        sort_open_list(OPEN)

    print(" No solution found.")

# ===== DRIVER CODE =====

n = int(input("Enter the board size (e.g., 3 for 3x3): "))

print("\nEnter Start Configuration of board (use '_' for blank):")
Start = accept(n)

print("\nEnter Goal Configuration of board (use '_' for blank):")
Goal = accept(n)

play_game(Start, Goal, n)

"""
🧠 What Is the 8-Puzzle Problem?
It's a classic sliding puzzle with 8 numbered tiles and one blank (_) space on a 3x3 board.

The goal is to reach a desired tile arrangement (goal state) from a given start configuration using legal moves (up, down, left, right).

🌟 What Is A (A-Star) Algorithm?*
A* is a path-finding algorithm that uses:

g(n): cost from the start node to current node n

h(n): estimated cost from n to the goal (heuristic)

f(n) = g(n) + h(n): total estimated cost of the solution through node n

It chooses the path that minimizes f(n).

🧩 How Your Code Works (Step by Step):
1. Input & Setup:
User provides:

Start configuration

Goal configuration

Board is stored as a 2D list.

2. *A Core Loop (play_game)**:
Maintains an OPEN list (nodes to explore) and a CLOSED list (already explored).

Each node stores:

The current board (Current)

g(n) → move count (depth/level)

f(n) → total cost

3. Heuristic (h_score):
Uses misplaced tiles heuristic: counts how many tiles are not in the correct position (excluding _).

4. Child Generation (move_gen):
Finds the blank tile.

Generates all possible moves (left, right, up, down).

Computes new f(n) for each child.

5. Selection:
Children are added to OPEN.

OPEN is sorted by lowest f(n) — ensures best path is chosen next.

6. Goal Check:
If current state equals the goal, the puzzle is solved.

If OPEN is empty and goal not found, no solution exists.

📌 Summary:
Component	Description
g(n)	Number of moves made from start
h(n)	Misplaced tile count heuristic
f(n)	Sum of g(n) and h(n) to prioritize paths
OPEN	Priority queue of nodes to explore
CLOSED	Stores already explored nodes
shuffle()	Swaps blank tile to simulate movement
goal_test()	Checks if current state matches the goal

🏁 Output:
Shows each board configuration at every step.

Displays total moves when the goal is reached."""
""
1 2 3
4 _ 6
7 5 8



1 2 3
4 5 6
7 8 _
""