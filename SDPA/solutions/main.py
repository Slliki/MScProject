# main.py:	This file runs the Tron game making use of the Board and Player(and children) classes
#			It presents the Game menu allowing for different game options

from board import Board
from player import Player

# main game menu loop
while (True):

    # board size input and validation loop
    while True:
        try:
            # capture the board size for the game from the user input
            board_size = int(input("Input board size (greater than 3): "))
            if board_size <= 3:
                print("Board size must be bigger than 3")
            else:
                # break out of the board size input and validation loop
                break
        except ValueError:
            print("Please enter a valid number.")

        # return to the board size input and validation loop

    # initialise the board instance with the size
    tron_board = Board(board_size)

    # create two objects of the player class
    # set the starting position for the players  (this can be an input too)
    player1 = Player("1", 0, 0, tron_board)

    # set the starting position for the player two at the right bottom corner 
    player2 = Player("2", board_size - 1, board_size - 1, tron_board)

    # print the board game start state with the 2 players in their initial positions
    print(tron_board)

    # game play loop
    valid_move = True
    while (valid_move):
        for player in [player1, player2]:
            # Get the player's move from the user
            move = ""
            while move not in ["l", "r", "u", "d"]:
                move = input(f'{player.name} - enter your move (u, d, l, r): ')
            valid_move = player.move(move)
            if valid_move == False:
                break

    # Break if not playing again
    play_again = input("Would you like to pay again? (y or n): ")
    if (play_again.lower() != 'y' and play_again.lower() != 'yes'):
        print("Thanks for playing, end of the game")
        break
