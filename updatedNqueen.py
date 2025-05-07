class NQueens:
    def __init__(self):
        self.n = int(input("Enter the value of n (number of queens): "))
        self.board = [-1] * self.n
        self.solutions = []

        # Branch and Bound helpers
        self.columns_used = [False] * self.n
        self.diag1_used = [False] * (2 * self.n - 1)  # row + col
        self.diag2_used = [False] * (2 * self.n - 1)  # row - col + n - 1

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
            diag1 = row + col
            diag2 = row - col + self.n - 1

            # Branch and Bound pruning + safety check
            if self.is_safe(row, col) and \
               not self.columns_used[col] and \
               not self.diag1_used[diag1] and \
               not self.diag2_used[diag2]:

                # Place queen and mark constraints
                self.board[row] = col
                self.columns_used[col] = True
                self.diag1_used[diag1] = True
                self.diag2_used[diag2] = True

                self.place_queen(row + 1)

                # Backtrack
                self.board[row] = -1
                self.columns_used[col] = False
                self.diag1_used[diag1] = False
                self.diag2_used[diag2] = False

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

"""✅ Now this code does:
Backtracking (via recursion and is_safe())

Branch and Bound (using constraint arrays for columns and diagonals)

This version matches the assignment requirement:
""""Implement a solution for a Constraint Satisfaction Problem using Branch and Bound and Backtracking for the N-Queens problem."


##########
""" Theory: CSP using Backtracking and Branch and Bound for N-Queens
The N-Queens problem is a classic Constraint Satisfaction Problem (CSP) where the goal is to place n queens on an n × n chessboard such that no two queens attack each other — meaning no two are in the same row, column, or diagonal.

To solve this, we use:

✅ Backtracking
It tries placing queens row by row.

At each step, it checks whether placing a queen is safe using the is_safe() method.

If a placement causes a conflict, it backtracks and tries another position.

✅ Branch and Bound
Adds an optimization to avoid checking impossible placements.

We use boolean arrays to track which columns and diagonals are already used.

If a queen threatens a used column or diagonal, we prune (skip) that branch early.

This makes the search much faster, especially for larger boards.

✅ Combined Approach
Together, Backtracking ensures correctness, and Branch and Bound improves efficiency by eliminating bad choices early — solving the N-Queens CSP more effectively."""