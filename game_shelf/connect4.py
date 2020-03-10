
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
                consec += 1
                if consec == 4:
                    return 1
            else:
                consec = 0
            row -= 1
            col += 1

    for coords in win_diags_ul:
        row, col = coords[0],coords[1]
        consec = 0
        while row >= 0 and col <= 6:
            if board[row][col] == piece:
                consec += 1
                if consec == 4:
                    return 1
            else:
                consec = 0
            row -= 1
            col -= 1
    return 0


def check_row_win(board, piece):
    # Win horizontally
    for row in board:
        consec = 0
        for slot in row:
            if slot == piece:
                consec += 1 #This is the same as consec = consec + 1
                if consec == 4:
                    return 1
            else:
                consec = 0

    return 0


class connect_four_board:
    '''
    This implements the basic connect4 board. It can place pieces, change players, and check if a particular player has won
    '''
    def __init__(self):
        self.board_state = [['*' for i in range(7)] for j in range(6)]
        self.players = ['X','O']
        self.current_turn = 0

    def print_state(self):
        '''
        Pretty prints the current state of the board, including whose turn it is
        '''
        print("It's currently " + str(self.players[self.current_turn]) + " to play")
        index = ['0', '1', '2', '3', '4', '5', '6']
        l = "    " + "   ".join(index) + " "
        print(l)

        for i in range(len(self.board_state)):
            if i == (len(self.board_state) - 1):
                l = str(i) + " |_" + "_|_".join(self.board_state[i]).replace("*", " ") + "_|"
            else:
                l = str(i) + " | " + " | ".join(self.board_state[i]).replace("*", " ") + " |"
            print(l)

    def get_state(self):
        '''
        Returns the state of the board for inspection
        '''
        full_state = {'board':self.board_state, 'player': self.players[self.current_turn]}
        return full_state

    def play_turn(self, col):
        '''
        Places a piece on the board in the selected column for the current player
        Returns -1 for illegal moves, returns 0 otherwise
        '''
        if self.board_state[0][col] != '*':
            # Illegal move
            return -1

        piece = self.players[self.current_turn]
        row = 0
        while self.board_state[row][col] == '*':
            row += 1
            if row == len(self.board_state):
                break
        self.board_state[row-1][col] = piece
        return 1

    def change_player(self):
        '''
        Changes whose turn it is
        '''
        self.current_turn = self.current_turn ^ 1

    def check_win(self):
        '''
        Checks if the current player has won
        '''
        piece = self.players[self.current_turn]
        if check_row_win(self.board_state, piece) == 1:
            return 1

        # A vertical win is just a horizontal win, transpose the board and run a horizontal check
        v_board = [list(i) for i in zip(*self.board_state)]
        if check_row_win(v_board, piece) == 1:
            return 1

        # A diagonal win is a bit more involved, see the helper function above
        if check_win_by_diag(self.board_state, piece) == 1:
            return 1

        return 0
