# Chess-Game

This project is the regular game of chess written in Python.
The code is all my own.

Enjoy.

## Project Goals
1) Adding a simple algorithm which will be used as an Artifiical Intelligence that the player can play against. 
   - The algorithm should eventually be able to include different difficulties for the player to choose to play against.
2) Add more comments to the code to make sure that each line is accounted or, and is easy to understand. 
3) Simplifying the code.
   - Meaning, reducing the amount of code in the file so as to make sure that it's easy to understand and navigate.
      - All repeated code should be placed in fuctions, so as to make it easier to be reused, without having to re-write each time that its needed. 
4) Debugging the movement of the pieces. 
   - Test the game to see if the movement of the pieces works as it should. 
   - Implament the "nearby system" to each movement of the pieces. 
5) Merge the Queen and King functions with one another. 
   - Make sure to merge the code for the queen and king functions into one so as to increase code simplicity. 

## Completed Goals
1) Chess Board
2) Current Movement Functionality
   - Pawn Movement functionality has been completed. 
   - Rook Movement functionality has been completed. 
   - Knight Movement functionality has been completed. 
3) Simplyifying code
   - Repeated code has been placed in a function which can now be used to remove the necessity of copying it, and pasting it 10 times over in the program. 
4) Add a fucntion in the class which is used to determine if there is a piece in front of you (which is from your own team).
   - If there is, a message has to come up telling the player that they're not allowed to move there.
   - If there isn't, then nothing happens. 
5) Finishing the movement functionality of all pieces on the chess board.
   - The movement for each piece has been completed and added to the code.
6) Debugging
   - Fixed the "desired_choice" to "self.desired_choice".
   - Fixed more "self.".
   - Fixed "queen_move" call error. 
