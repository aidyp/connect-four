import game_shelf/connect4 as c4

def play_game():
    new_game = c4.connect_four_board()
    new_game.print_state()
    new_game.play_turn(3)
    new_game.change_player()
    new_game.print_state()
