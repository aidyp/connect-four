
def check_win_by_diag(board, piece):
    '''
    This checks for a diagonal win
    '''

    # No need to dynamically generate the diagonals #

def initialise_board():
    board = [['*' for i in range(7)] for j in range(6)]
    return board

def print_board(board):
    '''
    Pretty print the board
    '''
    index = ['0', '1', '2', '3', '4', '5', '6']
    l = "  " + "   ".join(index) + " "
    print(l)

    for i in range(len(board)):
        if i == (len(board) - 1):
            l = "|_" + "_|_".join(board[i]).replace("*", " ") + "_|"
        else:
            l = "| " + " | ".join(board[i]).replace("*", " ") + " |"
        print(l)

def place_piece(board, piece, index):
    '''
    Inserts a piece into the board, if possible
    '''

    if board[0][index] != '*':
        #Illegal move
        return 0

    col = 0
    while board[col][index] == '*':
        col += 1
        if col == len(board):
            break
    board[col-1][index] = piece
    return 1

def check_row_win(board, piece):
    # Win horizontally
    for row in board:
        for slot in row:
            if slot == piece:
                consec += 1
                if consec == 4:
                    return 1
            else:
                consec = 0

    return 0

def check_win(board, piece):
    '''
    Checks if a piece has won a game, usually called after a piece has been placed
    '''
    if check_row_win(board, piece) == 1:
        return 1
    # A vertical win is just a horizontal win, transpose the board and run the check
    v_board = [list(i) for i in zip(*board)]
    if check_row_win(v_board, piece) == 1:
        return 1

    # Diagonal win is a bit more involved. Suspect easiest is just to hardcode the diagonals and check then
    # Stack overflow says change the co-ordinate scheme


def test_vertical(game_board):
    for i in range(0, 4):
        d = place_piece(game_board, 'X', 3)
    return check_win(game_board, 'X')

def test_horizontal(game_board):
    for i in range(0, 4):
        d = place_piece(game_board, '0', i)
    return check_win(game_board, '0')

game_board = initialise_board()
print_board(game_board)
place_piece(game_board, 'X', 3)
print_board(game_board)
place_piece(game_board, 'O', 3)
print_board(game_board)
