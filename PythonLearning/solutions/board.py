# board.py This file contains the Board class

class Board:
    """ validate player move, plot player paths and print the board.

    Works out whether a player has won, lost or drawn (drawn in simultaneous mode).
    In simultaneous mode, the board is only shown after both players have moved. """

    def __init__(self, size):
        """ initialise the Board instance with name, size , game option and game mode.

		parameters:
		size - size of the board in length (board is a square)

		returns the initialized board instance """

        self.size = size
        self.grid = [[" " for i in range(size)] for j in range(size)]
        # 使用一般的for循环
        # self.grid = []
        # for i in range(size):
        #     row = []
        #     for j in range(size):
        #         row.append(" ")
        #     self.grid.append(row)

    # print the board, overwriting the __str__ built in function
    def __str__(self):
        """ print the Board instance's current state using the board grid variable. """
        s = ""
        s += "-" * (self.size * 2 + 1) + "\n"
        for row in self.grid:
            s += "|" + ("|".join(str(x) for x in row) + "|") + "\n"
        s += "-" * (self.size * 2 + 1) + "\n"
        return s

    def update_board(self, value, x, y):
        """ place the trail or player character on the board.

		parameters:
		value- current player, This could be the players new position or the players trail
		x- row position on the board to place the character
		y - column position on the board to place the character """

        self.grid[y][x] = value

    def is_valid_move(self, player_name, target_row, target_col):
        """ validate the current player's move.

        A valid move will result in the board state being re-printed
        In simultaneous mode, print the board state only after both players have moved

		parameters:
		player_name - current player's name
		target_row - current player's intended row position on the board
		target_col - current player's intended column position on the board
		
		returns:
		the validation result - True for a valid move, False for an invalid move
		 """

        # player loses when moving off the board
        if target_row < 0 \
                or target_row >= self.size \
                or target_col < 0 \
                or target_col >= self.size:
            print("Game Over - Player " + player_name + " has lost (collided to the wall)")
            return False

        # player loses when moving into another player or a trail
        if self.grid[target_col][target_row] != " ":
            print("Game Over - Player " + player_name + " has lost, collided to a current path")
            return False

        # plot player's new position and a trail character in it's previous position 
        self.update_board(player_name, target_row, target_col)

        # print __str__ (the current board after update)
        print(self)

        # valid move, blank is message returned
        return True
