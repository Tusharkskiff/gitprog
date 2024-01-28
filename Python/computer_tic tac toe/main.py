import easy_ai as e
import difficult_ai as d

# welcome
print("-" * 60)
print("WELCOME TO TIC TAC TOE")
print("-" * 60)

# making choice of difficulty and icon
print()
print("Choose your difficulty")
print("1)EASY      2)Difficulty")
choice = int(input("Choose your difficulty level ( 1 or 2 )  : "))
print()
symbol = input("Choose the symbol ( X / O ):  ")
symbol = symbol.upper()
if symbol == "X" or symbol == "O":
    if choice == 1:
        e.easy(symbol)
    elif choice == 2:
        d.difficult(symbol)
else:
    print("invalid input")
