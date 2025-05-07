class NQueens:
    def __init__(self):
        self.n = int(input("Enter the value of n (number of queens): "))
        self.board = [-1] * self.n
        self.solutions = []

    def is_safe(self, row, col):
        for i in range(row):
            if self.board[i] == col or \
               self.board[i] - i == col - row or \
               self.board[i] + i == col + row:
                return False
        return True

    def place_queen(self, row):
        if row == self.n:
            self.solutions.append(self.board[:])
            return
        for col in range(self.n):
            if self.is_safe(row, col):
                self.board[row] = col
                self.place_queen(row + 1)
                self.board[row] = -1  # Backtrack

    def find_output(self):
        self.place_queen(0)

    def print_output(self):
        if not self.solutions:
            print("No solutions found!")
        else:
            for index, solution in enumerate(self.solutions, start=1):
                print(f"Solution {index}:")
                for row in range(self.n):
                    board_row = ['Q' if col == solution[row] else '.' for col in range(self.n)]
                    print(' '.join(board_row))
                print("\n")
            print(f"Total number of solutions: {len(self.solutions)}")

# Run the solver
solver = NQueens()
solver.find_output()
solver.print_output()

"""n-Queens Problem: Branch and Bound vs. Backtracking
1. Backtracking:
Idea: Place queens one by one in different rows, backtracking when a conflict occurs (same column or diagonal).

Process:

Place a queen in a row.

Move to the next row and place a queen in a valid position.

If no valid position, backtrack to the previous row and try the next position.

Repeat until all queens are placed or all possibilities are explored.

Time Complexity: O(n!) in the worst case, as it explores all potential placements.

Use: Simple and effective for smaller values of n.

2. Branch and Bound:
Idea: Uses a search tree with pruning to avoid exploring unpromising branches.

Process:

Place queens in rows, but also compute a bounding function to track conflicts.

If a partial solution exceeds the current best (in terms of conflicts), prune the branch.

Continue exploring promising branches until a solution is found.

Time Complexity: O(n!) in the worst case, but often faster than backtracking due to pruning.

Use: More efficient for larger n due to pruning.

Key Differences:
Backtracking: Simple, but can explore many unneeded solutions.

Branch and Bound: More complex, but prunes unpromising solutions, improving efficiency."""