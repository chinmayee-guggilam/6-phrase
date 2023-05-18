'''Knight’s Tour Problem'''
#code
# Function to check if a move is valid
def is_valid_move(x, y, board, n):
    if x >= 0 and x < n and y >= 0 and y < n and board[x][y] == -1:
        return True
    return False

# Function to find the next valid move
def find_next_move(x, y, board, n, move_x, move_y):
    min_degrees = n + 1
    min_index = -1

    for i in range(8):
        next_x = x + move_x[i]
        next_y = y + move_y[i]

        if is_valid_move(next_x, next_y, board, n):
            count = 0
            for j in range(8):
                new_x = next_x + move_x[j]
                new_y = next_y + move_y[j]
                if is_valid_move(new_x, new_y, board, n):
                    count += 1

            if count < min_degrees:
                min_degrees = count
                min_index = i

    if min_index != -1:
        x += move_x[min_index]
        y += move_y[min_index]
        board[x][y] = board[x][y-1] + 1

    return x, y

# Function to solve the Knight's Tour problem
def knights_tour(n):
    # Initialize the board
    board = [[-1 for _ in range(n)] for _ in range(n)]
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]

    # Start at position (0, 0)
    x = 0
    y = 0
    board[x][y] = 0

    # Perform the tour
    for _ in range(n*n - 1):
        x, y = find_next_move(x, y, board, n, move_x, move_y)

    # Print the solution
    for row in board:
       
