A Python Tutorial to create a Craps function

1) Open an empty file in Python
- Open up IDLE, a Python app. (Python 3 preferred). After opening IDLE, create a new file. Name this file craps.py
2) Inform the user how craps is played
- After creating our new file, create a function (printIntro()) that will introduce the user to how Craps is played. This can be done with multiple print statements.

3) Generate the random number generator
- Import the random utility; and from random import the file randint.

4) Define the function
- Create the craps () function and call the function printIntro().

5) Create the player’s first roll
- To simulate the first dice roll in craps, create two different integers (random 1-6), save those integers, and then add them together. For this example, I utilized the variables x, y, and roll = x + y.

6) Did the game end?
- Use if, elif, or else statements to establish whether the game has ended. If the plyer has rolled 2,3,12, the player has lost. Else If the player has rolled 7 or 11, they have won the game. Else the game continues to go.

7) Continue the game
- Create a new set of conditions to recreate a second roll. Assign second roll to new variables (x2 and y2), and newRoll = x2 + y2.

8) Second Phase: Another Set of Rules
- If the player rolls 7 they have lost. They will only win if they make the point. Create a while loop function that will end with either parameter being met.
