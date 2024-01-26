import game_src as gc
from random import randrange

def difficult(symbol):
    
    def ais(human,ai):
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

            rw=gc.rocky(ai)
            if rw==False:
                gc.diffai(human,ai)
            if gc.is_victory(ai):
                gc.print_board()
                print("AI Wins! Congratulations!")
                break
            elif gc.is_draw():
                print("Its a draw!")
                break
            
    

    def aif(human,ai):
        print("still in progress")


    if symbol=='X':
        human=symbol
        ai='O'
        ais(human,ai)
        
    elif symbol=='O':
        human=symbol
        ai='X'
        aif(human,ai)