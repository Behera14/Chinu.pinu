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
This code solves the 8-puzzle problem using the A* (A-star) search algorithm. Here's what each key function does and how it fits into A*:

Function	Purpose	A* Role
accept()	Takes input for start and goal states	Input stage
print_board()	Prints the puzzle	For user display
find_space()	Finds the position of the blank space ('_')	Needed for legal moves
shuffle()	Moves the blank to generate a new state	Creates children
copy_current()	Makes a deep copy of the board	Avoid mutation of boards
h_score()	Heuristic function: counts misplaced tiles	A* uses this as h(n)
g_score()	Path cost: number of steps taken so far	A* uses this as g(n)
f_score()	Total cost: f(n) = g(n) + h(n)	Core of A* algorithm
move_gen()	Generates all valid children states	Expands current node
goal_test()	Checks if current state matches goal	Termination condition
sort_open_list()	Sorts OPEN list based on f(n)	Priority queue behavior
play_game()	Main function that implements A*	Search loop

✅ 2. Theory: How Is This Related to the Statement?
🔷 Statement:
"Implement A* algorithm for 8 puzzle problem"

🔷 Theory:
The 8-puzzle is a classic search problem where the agent moves tiles on a 3×3 board to reach a goal configuration.
 It is solved efficiently using A*, a best-first search algorithm.

🔑 A* Search Algorithm:
A* uses:

g(n): The cost from the start node to the current node.

h(n): The estimated cost from the current node to the goal (heuristic).

f(n) = g(n) + h(n): Total estimated cost through node n.

A* maintains:

An OPEN list of nodes to explore.

A CLOSED list of already-explored nodes.

It always chooses the node with the lowest f(n) from the OPEN list, making it both optimal and efficient, if h(n) is admissible.

🔗 Code and Theory Connection:
Your code calculates f(n) in f_score(), combining real path cost g(n) and heuristic h(n).

It generates valid next states using move_gen(), adds them to the OPEN list, and explores them in order of lowest f(n) using sort_open_list().

It prints the path step-by-step and stops when the goal state is reached.

✅ Summary:
This code correctly implements the A* algorithm for solving the 8-puzzle problem using:

Misplaced tile heuristic for estimating distance.

Priority-based search guided by f(n).

Backtracking and state expansion via child generation.
""
1 2 3
4 _ 6
7 5 8



1 2 3
4 5 6
7 8 _
"""""