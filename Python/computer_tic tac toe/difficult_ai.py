import game_src as gc
import random

#function for difficult level ai 
def difficult(symbol):
    #function for ai playing as X
    def ais(human, ai):
        gc.print_board()
        gc.player_move(human)
        gc.print_board()
        gc.play(ai)
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

            rw = gc.rocky(ai)
            if rw == False:
                gc.diffai(human, ai)
            if gc.is_victory(ai):
                gc.print_board()
                print("AI Wins! Congratulations!")
                break
            elif gc.is_draw():
                print("Its a draw!")
                break

    #function for human playing as X
    def aif(human, ai):
        gc.print_board()
        gc.lily(human, ai)
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

            rw = gc.rocky(ai)
            if rw == False:
                gc.diffai(human, ai)
            if gc.is_victory(ai):
                gc.print_board()
                print("AI Wins! Congratulations!")
                break
            elif gc.is_draw():
                gc.print_board()
                print("Its a draw!")
                break

    ##############################
    #assigning symbols for ai and human and calling the starting function
    if symbol == "X":
        human = symbol
        ai = "O"
        ais(human, ai)

    elif symbol == "O":
        human = symbol
        ai = "X"
        aif(human, ai)
