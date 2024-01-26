#creating the board
import random
board = ["  " for i in range(9)]

#Function to print board
def print_board():
        row1 = "| {} | {} | {} |".format(board[0], board[1], board[2])
        row2 = "| {} | {} | {} |".format(board[3], board[4], board[5])
        row3 = "| {} | {} | {} |".format(board[6], board[7], board[8])

        print()
        print(row1)
        print(row2)
        print(row3)
        print()


def player_move(icon):
    
    try:
        print("Your turn player {}".format(icon))
        choice = int(input("Enter your move (1-9): ").strip())
    except ValueError:
        print("invalid input")
        print()
        player_move(icon)
    else:
        if choice>0 and choice<10:
            
            if board[choice -1] == "  ":
                board[choice -1 ] = icon
            else:
                print("That space is taken!")
                print()
                player_move(icon)
        else:
            print("Invalid input")
            print()
            player_move(icon)

#easy bot moves
def play(ai):
        move=random.choice([0,1,2,3,4,5,6,7,8])
        
        if move>=0 and move<10:
            if board[move] == "  ":
                print("AI playes at {} ".format(move+1))
                board[move] = ai
            else:
                play(ai)


#function that checks for the victory of the game
def is_victory(icon):
    if (board[0] == icon and board[1] == icon and board[2] == icon) or \
       (board[3] == icon and board[4] == icon and board[5] == icon) or \
       (board[6] == icon and board[7] == icon and board[8] == icon) or \
       (board[0] == icon and board[3] == icon and board[6] == icon) or \
       (board[1] == icon and board[4] == icon and board[7] == icon) or \
       (board[2] == icon and board[5] == icon and board[8] == icon) or \
       (board[0] == icon and board[4] == icon and board[8] == icon) or \
       (board[2] == icon and board[4] == icon and board[6] == icon):
        return True
    else:
        return False


#function that checks if the game is a draw    
def is_draw():
    if "  " not in board:
        return True
    else:
        return False


def rocky(ai):
        if board[0]==ai and board[1]==ai:
                if board[2] == "  ":
                        print("AI playes at 3")
                        board[2] = ai
                        return True
        if board[0]==ai and board[2]==ai:
                if board[1] == "  ":
                        print("AI playes at 2")
                        board[1] = ai
                        return True
        if board[1]==ai and board[2]==ai:
                if board[0] == "  ":
                        print("AI playes at 1")
                        board[0] = ai
                        return True
        if board[3]==ai and board[4]==ai:
                if board[5] == "  ":
                        print("AI playes at 6")
                        board[5] = ai
                        return True
        if board[3]==ai and board[5]==ai:
                if board[4] == "  ":
                        print("AI playes at 5")
                        board[4] = ai
                        return True
        if board[4]==ai and board[5]==ai:
                if board[3] == "  ":
                        print("AI playes at 4")
                        board[3] = ai
                        return True
        if board[6]==ai and board[7]==ai:
                if board[8] == "  ":
                        print("AI playes at 9")
                        board[8] = ai
                        return True
        if board[6]==ai and board[8]==ai:
                if board[7] == "  ":
                        print("AI playes at 8")
                        board[7] = ai
                        return True
        if board[7]==ai and board[8]==ai:
                if board[6] == "  ":
                        print("AI playes at 7")
                        board[6] = ai
                        return True

                

        if board[0]==ai and board[3]==ai:
              if board[6] == "  ":
                    print("AI playes at 7")
                    board[6] = ai
                    return True
        if board[0]==ai and board[6]==ai:
                if board[3] == "  ":
                    print("AI playes at 4")
                    board[3] = ai
                    return True
        if board[3]==ai and board[6]==ai:
                if board[0] == "  ":
                    print("AI playes at 1")
                    board[0] = ai
                    return True
        if board[1]==ai and board[4]==ai:
              if board[7] == "  ":
                    print("AI playes at 8")
                    board[7] = ai
                    return True
        if board[1]==ai and board[7]==ai:
                if board[4] == "  ":
                    print("AI playes at 5")
                    board[4] = ai
                    return True
        if board[4]==ai and board[7]==ai:
                if board[1] == "  ":
                    print("AI playes at 2")
                    board[1] = ai
                    return True
        if board[2]==ai and board[5]==ai:
              if board[8] == "  ":
                    print("AI playes at 9")
                    board[8] = ai
                    return True
        if board[2]==ai and board[8]==ai:
                if board[5] == "  ":
                    print("AI playes at 6")
                    board[5] = ai
                    return True
        if board[5]==ai and board[8]==ai:
                if board[2] == "  ":
                    print("AI playes at 3")
                    board[2] = ai
                    return True

                

                
        if board[0]==ai and board[4]==ai:
                if board[8] == "  ":
                    print("AI playes at 9")
                    board[8] = ai
                    return True
        if board[0]==ai and board[8]==ai:
                if board[4] == "  ":
                    print("AI playes at 5")
                    board[4] = ai
                    return True
        if board[4]==ai and board[8]==ai:
                if board[0] == "  ":
                    print("AI playes at 1")
                    board[0] = ai
                    return True
                
        if board[2]==ai and board[4]==ai:
                if board[6] == "  ":
                    print("AI playes at 7")
                    board[6] = ai
                    return True
        if board[2]==ai and board[6]==ai:
                if board[4] == "  ":
                    print("AI playes at 5")
                    board[4] = ai
                    return True
              
        if board[4]==ai and board[6]==ai:
                if board[2] == "  ":
                    print("AI playes at 3")
                    board[2] = ai
                    return True
        else:
                return False



################################################

def diffai(human,ai):
        if board[0]==human and board[1]==human:
                if board[2] == "  ":
                        print("AI playes at 3")
                        board[2] = ai
                        return
        if board[0]==human and board[2]==human:
                if board[1] == "  ":
                        print("AI playes at 2")
                        board[1] = ai
                        return
        if board[1]==human and board[2]==human:
                if board[0] == "  ":
                        print("AI playes at 1")
                        board[0] = ai
                        return
        if board[3]==human and board[4]==human:
                if board[5] == "  ":
                        print("AI playes at 6")
                        board[5] = ai
                        return
        if board[3]==human and board[5]==human:
                if board[4] == "  ":
                        print("AI playes at 5")
                        board[4] = ai
                        return
        if board[4]==human and board[5]==human:
                if board[3] == "  ":
                        print("AI playes at 4")
                        board[3] = ai
                        return
        if board[6]==human and board[7]==human:
                if board[8] == "  ":
                        print("AI playes at 9")
                        board[8] = ai
                        return
        if board[6]==human and board[8]==human:
                if board[7] == "  ":
                        print("AI playes at 8")
                        board[7] = ai
                        return
        if board[7]==human and board[8]==human:
                if board[6] == "  ":
                        print("AI playes at 7")
                        board[6] = ai
                        return

                

        if board[0]==human and board[3]==human:
              if board[6] == "  ":
                    print("AI playes at 7")
                    board[6] = ai
                    return
        if board[0]==human and board[6]==human:
                if board[3] == "  ":
                    print("AI playes at 4")
                    board[3] = ai
                    return
        if board[3]==human and board[6]==human:
                if board[0] == "  ":
                    print("AI playes at 1")
                    board[0] = ai
                    return
        if board[1]==human and board[4]==human:
              if board[7] == "  ":
                    print("AI playes at 8")
                    board[7] = ai
                    return
        if board[1]==human and board[7]==human:
                if board[4] == "  ":
                    print("AI playes at 5")
                    board[4] = ai
                    return
        if board[4]==human and board[7]==human:
                if board[1] == "  ":
                    print("AI playes at 2")
                    board[1] = ai
                    return
        if board[2]==human and board[5]==human:
              if board[8] == "  ":
                    print("AI playes at 9")
                    board[8] = ai
                    return
        if board[2]==human and board[8]==human:
                if board[5] == "  ":
                    print("AI playes at 6")
                    board[5] = ai
                    return
        if board[5]==human and board[8]==human:
                if board[2] == "  ":
                    print("AI playes at 3")
                    board[2] = ai
                    return

                

                
        if board[0]==human and board[4]==human:
                if board[8] == "  ":
                    print("AI playes at 9")
                    board[8] = ai
                    return
        if board[0]==human and board[8]==human:
                if board[4] == "  ":
                    print("AI playes at 5")
                    board[4] = ai
                    return
        if board[4]==human and board[8]==human:
                if board[0] == "  ":
                    print("AI playes at 1")
                    board[0] = ai
                    return
                
        if board[2]==human and board[4]==human:
                if board[6] == "  ":
                    print("AI playes at 7")
                    board[6] = ai
                    return
        if board[2]==human and board[6]==human:
                if board[4] == "  ":
                    print("AI playes at 5")
                    board[4] = ai
                    return
              
        if board[4]==human and board[6]==human:
                if board[2] == "  ":
                    print("AI playes at 3")
                    board[2] = ai
                    return
        else:
                play(ai)
