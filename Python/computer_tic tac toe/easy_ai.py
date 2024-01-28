import game_src as gc
from random import randrange

#function for easy level ai 
def easy(symbol):

    #defining symboly for human and ai
    if symbol == "X":
        human = "X"
    else:
        human = "O"

    while True:
        if human == "X":
            ai = "O"
            # infinite loop to play for human first
            while True:
                gc.print_board()
                gc.player_move(human)
                gc.print_board()
                if gc.is_victory(human):
                    print("YOU Wins! Congratulations!")
                    break
                elif gc.is_draw():
                    print("Its a draw!")
                    break

                gc.play(ai)
                if gc.is_victory(ai):
                    gc.print_board()
                    print("AI Wins! Congratulations!")
                    break
                elif gc.is_draw():
                    print("Its a draw!")
                    break
            break

        else:
            ai = "X"
            # infinite loop to play for ai first
            while True:
                gc.print_board()
                gc.play(ai)
                gc.print_board()
                if gc.is_victory(ai):
                    print("AI Wins! Congratulations!")
                    break

                elif gc.is_draw():
                    print("Its a draw!")
                    break

                gc.player_move(human)
                if gc.is_victory(human):
                    gc.print_board()
                    print("Human Wins! Congratulations!")
                    break
                elif gc.is_draw():
                    print("Its a draw!")
                    break
            break
