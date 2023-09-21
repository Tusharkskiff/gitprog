# A classial game of hand cricket with the computer
# contains a bot that plays with you

import random


# Function to see who wins the toss
def toss_game():
    try:
        call=int(input("Heads(0) or tails(1) : "))
        if call>1 or call<0:
            raise ValueError
        
    except:
        print("Invalid call!! Retoss to be followed")
        toss_game()

    else:
        return call


# Function to choose bowling or batting by the winner of the toss (cpu or player)
def toss_selection(call):
    coin=random.randint(0,2) #AI
    
    if coin==call:
        print("Congratulations! You won the toss ")
        t=int(input("Would you like to bowl(0) or bat(1) :"))
        toss=toss_list[t]
        return toss,player_list[1]
    else:
        toss=random.choice(list(toss_list.values())) #AI
        return toss,player_list[0]
    

    
# A class function-> that is when the player bats first and cpu bowls first
def cpu_bowls_first_you_bat_first_A(): 
    
    print()
    print("YOUR BATTING NOW")
    print()

    your_total_score=0
    cpu_total_score=0

    while True:
        
        you_bat_hit=int(input("Enter your batting number (1 to 6) : "))

        if you_bat_hit>6 or you_bat_hit<1:
            print("You disrupted a canon event! As an anomaly we will exit the program byeee!!!")
            print()
            print(exit)
            exit(0)

        cpu_bowls=random.randint(1,6) #AI
            
        print("You -> {}    CPU -> {}".format(you_bat_hit,cpu_bowls))
            
        if you_bat_hit == cpu_bowls:
            print("Oopsies your OUT!! ")
            if your_total_score == 0:
                    print("---> Your a Golden Duck (T_T) <---")
            print("Your total score is: {}".format(your_total_score))
            print()
            print("Tagret set for cpu is {}".format(your_total_score+1))
            print()
            break
        else:
            your_total_score+=you_bat_hit
            if your_total_score % 50 == 0:
                print("---> Congrats on achievement :D <---")
            print("Your current score : {}".format(your_total_score))
            print()
    
    print("CPU to bat now")
    print("YOUR BOWLING NOW")

    while True:
        if your_total_score >= cpu_total_score:
            you_bowl=int(input("Enter your bowling number (1 to 6) : "))

            if you_bowl>6 or you_bowl<1:
                print("You disrupted a canon event! As an anomaly we will exit the program byeee!!!")
                print()
                print(exit)
                exit(0)

            cpu_bats=random.randint(1,6) #AI

            print("You -> {}    CPU -> {}".format(you_bowl,cpu_bats))
 
            if you_bowl == cpu_bats:
                print("Congo you got the wicket")
                if cpu_total_score == 0:
                    print("---> YOU got a golden duck :D <---")
                print("CPU got out at : {}".format(cpu_total_score))
                print()
                winner=1
                break
            else:
                cpu_total_score+=cpu_bats
                if cpu_total_score % 50 == 0:
                    print("---> CPU is playing great!! bowl well player <---")
                print("CPU current score : {}".format(cpu_total_score))
                print()
        else:
            print("CPU beat you")
            print()
            winner=0
            break
    return winner,your_total_score,cpu_total_score


        
        
        
# B class function -> that is when the player bowls first and cpu bats first
def cpu_bat_first_you_bowl_first_B():
    print()
    print("YOUR BOWLING NOW")
    print()

    your_total_score=0
    cpu_total_score=0

    while True:
            you_bowl=int(input("Enter your bowling number (1 to 6) : "))

            if you_bowl>6 or you_bowl<1:
                print("You disrupted a canon event! As an anomaly we will exit the program byeee!!!")
                print()
                print(exit)
                exit(0)

            cpu_bats=random.randint(1,6) #AI

            print("You -> {}    CPU -> {}".format(you_bowl,cpu_bats))

            if you_bowl == cpu_bats: 
                print("Congo you got the wicket")
                if cpu_total_score == 0:
                    print(" ---> YOU got a golden duck :D <---")
                print("CPU got out at : {}".format(cpu_total_score))
                print()
                print("Tagret for you is {}".format(cpu_total_score+1))
                print()
                break
            else:
                cpu_total_score+=cpu_bats
                if cpu_total_score % 50 == 0:
                    print("---> CPU is playing great!! bowl well player <---")
                print("CPU current score : {}".format(cpu_total_score))
                print()
    
    print("CPU to bowl now")
    print("YOUR BATTING NOW")

    while True:
        if cpu_total_score >= your_total_score:
        
            you_bat_hit=int(input("Enter your batting number (1 to 6) : "))

            if you_bat_hit>6 or you_bat_hit<1:
                print("You disrupted a canon event! As an anomaly we will exit the program byeee!!!")
                print()
                print(exit)
                exit(0)

            cpu_bowls=random.randint(1,6) #AI
            
            print("You -> {}    CPU -> {}".format(you_bat_hit,cpu_bowls))

            if you_bat_hit == cpu_bowls:
                print("Oopsies your OUT!! ")
                if your_total_score == 0:
                    print("---> Your a Golden Duck (T_T) <---")
                print("Your total score is: {}".format(your_total_score))
                print()
                winner=0
                break
            else:
                your_total_score+=you_bat_hit
                if your_total_score % 50 == 0:
                    print("---> Congrats on achievement :D <---")
                print("Your current score : {}".format(your_total_score))
                print()

        else:
            print("You beat CPU")
            print()
            winner=1
            break
    return winner,your_total_score,cpu_total_score



# Function to display the summary of game (winner and the game final scores)
def summary(winner):
    print()
    print("Summary:")
    print("YOU scored     CPU scored")
    print("    {}               {}".format(player_total_score,ai_total_score))

    if player_total_score == ai_total_score:
        print("Game drawn")
    elif winner==0:
        print("YOU LOST THE GAME!! Better luck next time")
    elif winner==1:
        print("Congratulations you won !!!!!! :D ")


#Starting of the game
print()
print("Welcome to hand cricket. Your opponet is the computer")
print()
print("_____________________________________________________________________________________________________________")
print("WARNING:type the number to make a selection.")
print("Head(0) type the number 0 to choose.")
print("The numbers in brackets are for making a selection.")
print("If incorrect numbers are typed the game would end !!")
print()
print("_____________________________________________________________________________________________________________")

print("All the best!! :D ")
print()
print("_____________________________________________________________________________________________________________")
print("Toss :")

toss_list={0:'Bowl',1:'Bat'}

play_ai={'Bowl':0,'Bat':1}

player_list={0:'CPU',1:'You'}

player_list_ai={'CPU':0,'You':1}

call=toss_game()
print("_____________________________________________________________________________________________________________")

selection,toss_winner=toss_selection(call)

print()
print("{} won the toss and chose to {}".format(toss_winner,selection))
print("_____________________________________________________________________________________________________________")


winner=-1

if player_list_ai[toss_winner]==0 and play_ai[selection]==0:
    #Cpu bowls first you bat first (A)
    winner,player_total_score,ai_total_score = cpu_bowls_first_you_bat_first_A()
    
elif player_list_ai[toss_winner]==0 and play_ai[selection]==1:
    #Cpu bats first you bowl first(B)
    winner,player_total_score,ai_total_score = cpu_bat_first_you_bowl_first_B()
    
elif player_list_ai[toss_winner]==1 and play_ai[selection]==0:
    #you bowl first cpu bats first(B)
    winner,player_total_score,ai_total_score = cpu_bat_first_you_bowl_first_B()
    
elif player_list_ai[toss_winner]==1 and play_ai[selection]==1:
    #you bat first cpu bowls first (A)
    winner,player_total_score,ai_total_score = cpu_bowls_first_you_bat_first_A()

summary(winner)
