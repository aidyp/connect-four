
def check_win_by_diag(board, piece):
    '''
    This checks for a diagonal win
    Return 1 if there is a win
    Return 0 if not
    '''
    # Work with Ronan to complete this section.
    # Current idea is to store a list of diagonal "roots", and check them in turn
    win_diags_ur = [(5,0)]
    win_diags_ul = [(5,6)]

    for coords in win_diags_ur:
        row, col = coords[0],coords[1]

        #Diagonal checking loop
        consec = 0
        while row >= 0 and col <= 6:
            if board[row][col] == piece:
                consec += 1:
            else:
                consec = 0
            row -= 1
            col += 1


def initialise_board():
    board = [['*' for i in range(7)] for j in range(6)]
    return board

def print_board(board):
    '''
    Pretty print the board
    '''
    index = ['0', '1', '2', '3', '4', '5', '6']
    l = "    " + "   ".join(index) + " "
    print(l)

    for i in range(len(board)):
        if i == (len(board) - 1):
            l = str(i) + " |_" + "_|_".join(board[i]).replace("*", " ") + "_|"
        else:
            l = str(i) + " | " + " | ".join(board[i]).replace("*", " ") + " |"
        print(l)

def place_piece(board, piece, index):
    '''
    Inserts a piece into the board, if possible
    '''

    if board[0][index] != '*':
        #Illegal move
        return 0

    row = 0
    while board[row][index] == '*':
        row += 1
        if row == len(board):
            break
    board[row-1][index] = piece
    return 1

def check_row_win(board, piece):
    # Win horizontally
    for row in board:
        for slot in row:
            consec = 0
            if slot == piece:
                consec += 1 #This is the same as consec = consec + 1
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


# Re-architect to form a class
class connect_four:
    '''
    This implements the basic connect4 board and equips it with the ability to place pieces
    and evaluate winners
    '''
    def __init___(self):
        self.state = initialise_board()
        self.players = ['X'. 'O']
        self.current_turn = 0

    def print_state(self):
        '''
        Prints the current state of the board, including who's turn it is
        '''
        print("It's currently " + str(self.players[self.current_turn]) + "to play")
        print_board()

    def get_state(self):
        '''
        Returns the state of the board for inspection
        '''
        full_state = {'board':self.state, 'player': self.players[self.current_turn]}
        return full_state

    def play_turn(self, col):
        '''
        Places a piece on the board in the selected column
        Returns -1 for illegal moves, returns 0 otherwise
        '''

    def change_player(self):
        self.current_turn ^= self.current_turn



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
