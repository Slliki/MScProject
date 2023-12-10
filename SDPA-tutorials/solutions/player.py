
# player.py: This file contains the Player and it's child classes (HumanPlayer, ComputerPlayer, SmartComputerPlayer)
# These classes get or generate a players move. 
# They make use of the Board class instance to validate and plot their move

from board import Board

class Player:
    def __init__ (self, name, x, y, board):
        """ initialise the Player instance with the players name, start position and board instance.

		parameters:
		name - player name. Used a the players board character
		x- player start row position on the board
		y - player start column position on the board
		board - instance of the board class. This will be used to invoke Board methods

		return the initialized Player instance """
		
        self.name =name
        self.x = x
        self.y = y
        self.board =board
        #update the board with the initial positions
        self.board.update_board(self.name, self.x, self.y)
        
    def move(self, direction):
        """ Validate the player direction and use the board instance to validate the move target.

		parameters:
		direction - direction of the player's move

		returns:
		the move target validation result - True for non-suicidal move, False for a move resulting in the end of the game
		the validation result information message """        
		# store potential new position (not validated yet)
        
        if direction == "l":
            self.x -= 1
        elif direction == "r":
            self.x += 1
        elif direction == "u":
            self.y -= 1
        elif direction == "d":
            self.y += 1
        
        #check whether this is the valid move on the baord
        return self.board.is_valid_move(self.name, self.x, self.y)
        
		


