import random
import time
roll = 0 #setting value of roll to 0
prenumber = 0 #setting value of prenumber to 0
gameover = False #assigning False to gameover

s1 = "- - - - -\n|       |\n|   O   |\n|       |\n- - - - -\n" #Dice roll graphics
s2 = "- - - - -\n| O     |\n|       |\n|     O |\n- - - - -\n"
s3 = "- - - - -\n| O     |\n|   O   |\n|     O |\n- - - - -\n"
s4 = "- - - - -\n| O   O |\n|       |\n| O   O |\n- - - - -\n"
s5 = "- - - - -\n| O   O |\n|   O   |\n| O   O |\n- - - - -\n"
s6 = "- - - - -\n| O   O |\n| O   O |\n| O   O |\n- - - - -\n"

def diceroll(roll): #function that rolls dice
    print("rolling.....")
    roll = random.randint(1,6) #generates a random number between 1 and 6
    return roll #returning the value of roll


def show_dice(roll): #function displays correct graphics
    if roll == 1: #if roll is equal to 1 then print coinciding graphic
        print(s1)
    elif roll == 2:#if roll is equal to 2 then print coinciding graphic
        print(s2)
    elif roll == 3:#if roll is equal to 3 then print coinciding graphic
        print(s3)
    elif roll == 4:#if roll is equal to 4 then print coinciding graphic
        print(s4)
    elif roll == 5:#if roll is equal to 5 then print coinciding graphic
        print(s5)
    elif roll == 6:#if roll is equal to 6 then print coinciding graphic
        print(s6)


#MAIN PROGRAM
print("The idea of this game is to roll the same number twice in a row")
print()
time.sleep(1) #1 second break

while gameover == False: #will loop whilst gameover is equal to False
    false = False #setting value of false to False
    print()
    ask = input("Type roll when you want to roll the dice") #user input

    if ask == "roll": #dice will not roll until user has entered "roll"
        roll = diceroll(roll) #assigned output of diceroll function to roll, calling function
        time.sleep(1) # 1 second break
        show_dice(roll) #calling show_dice function

    else: #if something other than roll is entered
        print()
        print("I do not understand") #display message to alert user
        print("please try again")
        false = True #set value of false to true so that this go does not count

    if prenumber == roll and false == False: #if you have rolled the same number twice in a row
        gameover = True
        print("you have rolled the same number twice in a row")
        print("you have won!!!")

    prenumber = roll #set prenumber to the value of roll, this means that the last number you rolled is stored
    

           

