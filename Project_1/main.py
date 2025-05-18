'''
1 =  rock
-1 = paper
0 = scissor
'''

import random


gameLoop = "yes"

# while loop to keep the game continued untill the user wants to exit.
while(gameLoop == "yes"):
    computer = random.choice([0, 1, -1])
    playDict = {"rock": 1, "paper": -1, "scissor": 0}
    playerChoice = input("Enter your choice: ")
    
    # handles input error by user
    if playerChoice not in playDict:
        print("Something went wrong. Please try again. ")
    else:

        playerMove = playDict[playerChoice]

        reverseDict= {1: "Rock", -1:"Paper", 0: "Scissor"}

        print(f"You have chosen {reverseDict[playerMove]} and the computer has chosen {reverseDict[computer]}")
        
        # conditions of the game
        
        if (computer == playerMove):
            print("Its a draw")
        else:    
            if(computer == -1 and playerMove == 0):
                print("You win")
            elif (computer == -1 and playerMove == 1):
                print("You loose")
            elif (computer == 1 and playerMove == -1):
                print("You win")
            elif(computer == 1 and playerMove == 0):
                print("You loose")
            elif(computer == 0 and playerMove == 1):
                print("You win")
            elif(computer == 0 and playerMove == -1):
                print("You loose")
                
    # condition for closing the loop              
    print("Do you want to continue? (yes or no):")
    gameLoop = input()

#exit game
print("....Game exited....Thanks")



        