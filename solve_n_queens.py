def is_square_valid(chess_board, row, column):
    chess_board_size = len(chess_board)

    # check if there is a queen in the row
    for column_index in range(column):
        if chess_board[row][column_index] == 1:
            return False
    
    i = row
    j = column

    # check upper-left diagonal
    while i >= 0 and j >= 0:
        if chess_board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    k = row
    l = column
    # check bottom-left diagonal
    while k < chess_board_size and l >= 0:
        if chess_board[k][l] == 1:
            return False
        k += 1
        l -= 1

    return True
    
def place_queens(chess_board, column):
    number_of_queens = len(chess_board)

    # base case since the queens are placed column by column
    if column >= number_of_queens:
        return True
    
    for row in range(number_of_queens):
        if is_square_valid(chess_board, row, column):
            chess_board[row][column] = 1
            if place_queens(chess_board, column + 1) == True:
                return True
            chess_board[row][column] = 0
    return False
    
def solve_n_queens_problem(number_of_queens):
    chess_board = [[0 for i in range(number_of_queens)] for j in range(number_of_queens)]
    if place_queens(chess_board, 0) == False:
        print("No solution")
    for i in range(len(chess_board)):
        for j in range(len(chess_board)):
            print(chess_board[i][j], end=" ")
        print()

if __name__ == '__main__':
    number_of_queens = 10
    solve_n_queens_problem(number_of_queens)
