# Write your code here :-)
import random;

#choices
game = ['rock', 'paper', 'scissors']



#Counting the number of wins of each player
user_wins = 0
comp_wins = 0

#determine the winner
def winorloss(comp_choice, user_choice):
    global comp_wins
    global user_wins
    if(comp_choice == 'rock'):
        if(user_choice == 'paper'):
            print("User won")
            user_wins = user_wins + 1
        elif(user_choice == 'scissors'):
            print("Computer wins")

            comp_wins = comp_wins + 1
        else:
            print("Draw!")


    elif(comp_choice == 'paper'):
        if(user_choice == 'scissors'):
            print("User won")

            user_wins = user_wins + 1
        elif(user_choice == 'rock'):
            print("Computer won")

            comp_wins = comp_wins + 1
        else:
            print("Draw!")


    else:
        if(user_choice == 'rock'):
            print("User won")

            user_wins = user_wins + 1
        elif(user_choice == 'paper'):
            print("Computer won")

            comp_wins = comp_wins + 1
        else:
            print("Draw!")


#play the game
while(True):

    a = int(input("Enter your choice: \n1. Rock 2. Paper 3. Scissors 4. Quit and Show score \n\n")) -1

    if(a != 3):
        user_choice = game[a]
        print("You chose: ", user_choice)
        comp_choice = random.choice(game)
        print("Computer chose: ", comp_choice)
        winorloss(comp_choice, user_choice)


    else:
        print("User:", user_wins)
        print("Computer:", comp_wins)
        print()
        if(user_wins < comp_wins):
            print("You have been defeated")
            print()
        elif(user_wins > comp_wins):
            print("You are victorious")
            print()
        else:
            print("Tournament draw!")
            print()
        break


