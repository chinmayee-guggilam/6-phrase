'''N Queen Problem'''
#Code
def solve_n_queens(n):
    # Initialize an empty chessboard
    chessboard = [['.' for _ in range(n)] for _ in range(n)]
    solutions = []

    def backtrack(row):
        # Base case: all queens have been placed
        if row == n:
            solutions.append([''.join(row) for row in chessboard])
            return

        for col in range(n):
            if is_safe(row, col):
                # Place the queen at the current position
                chessboard[row][col] = 'Q'
                # Recursively move to the next row
                backtrack(row + 1)
                # Remove the queen for backtracking
                chessboard[row][col] = '.'

    def is_safe(row, col):
        # Check if the current position is safe
        # by verifying no other queens threaten it
        for i in range(row):
            if chessboard[i][col] == 'Q':
                return False
            if col - (row - i) >= 0 and chessboard[i][col - (row - i)] == 'Q':
                return False
            if col + (row - i) < n and chessboard[i][col + (row - i)] == 'Q':
                return False
        return True

    # Start backtracking from the first row
    backtrack(0)

    return solutions


# Get the number of queens from the user
n = int(input("Enter the number of queens: "))

# Solve the N Queen problem
solutions = solve_n_queens(n)

# Print the solutions
print(f"Number of solutions: {len(solutions)}")
for i, solution in enumerate(solutions, 1):
    print(f"\nSolution {i}:")
    for row in solution:
        print(row)
