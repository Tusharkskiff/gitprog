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
        print("Your turn player ")
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