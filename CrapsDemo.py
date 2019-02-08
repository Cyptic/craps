#Craps for dummies! 
#Kyle Nelson

import random
from random import randint
import time


def printIntro():
    print('This program simulates the game of Craps. A game where')
    time.sleep(.8)
    print('the player rolls two six-sided die. If the initial roll is a')
    time.sleep(.8)
    print ('2, 3, or 12, the player immediately loses. If the roll is a 7 or 11')
    time.sleep(.8)
    print ('then the player  wins. Any other value and the game continues to the')
    time.sleep(.8)
    print ('second phase. In the sec ond phase, the player must roll the target number')
    time.sleep(.8)
    print ('to win; if they roll a 7 the player will lose.')
    time.sleep(1.0)
    print ('If the die is any value other than 7 or the target roll, the game continues.\n')
    

def craps():
    printIntro()
    time.sleep(2.0)
    x = randint (1,6)
    y = randint (1,6)
    roll = x + y
    
    
    if roll in {2,3,12}:
        print ("You rolled",roll)
        return "Oh no, You crapped out. You've lost your money!" 
    elif roll in {7,11}:
        print ("You rolled",roll)
        return "7-11! You've won the game!" 
    else:
        print("You rolled",roll)
        x2 = randint (1,6)
        y2 = randint (1,6)
        newRoll = x2 + y2
        if newRoll == roll:
            print ("You rolled",newRoll)
            return "You made your roll! You win!" 
        while True:
                if newRoll == 7:
                    time.sleep(1.3)
                    print ("You rolled",newRoll)
                    return "You didn't make your roll. You've lost your money!" 
                elif newRoll == roll:
                    print ("You rolled",newRoll)
                    time.sleep(1.1)
                    return "You made your roll! You win!" 
                else:
                    time.sleep(1.3)
                    print ("You rolled",newRoll)
                    x2 = randint (1,6)
                    y2 = randint (1,6)
                    newRoll = x2 + y2
                    

