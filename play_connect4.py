import game_shelf.connect4 as c4

def play_game():
    new_game = c4.connect_four_board()
    while True:
        new_game.print_state()
        move = input("Make your move: ")
        new_game.play_turn(move)
        if new_game.check_win() == 1:
            print("Player " + new_game.players[new_game.current_turn] + " Has won!")
            break
        new_game.change_player()


play_game()
