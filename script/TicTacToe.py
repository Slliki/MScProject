# This is a Tic Tac Toe game
# I will set 2 classes: Player and Board

class Board:
    def __init__(self):
        # board is a list of 9 empty strings, it represents the 9 cells(X or O) of the board
        self.board = [" " for _ in range(9)]

    def draw(self):
        # print the board
        print(self.board[0] + ' | ' + self.board[1] + ' | ' + self.board[2])
        print('---------')
        print(self.board[3] + ' | ' + self.board[4] + ' | ' + self.board[5])
        print('---------')
        print(self.board[6] + ' | ' + self.board[7] + ' | ' + self.board[8])

    def is_empty(self, position):
        # check if the cell is empty
        if self.board[position] == ' ':
            return True
        else:
            return False

    def set_chess(self, position, symbol):
        # set the chess on the board,it needs to check if the cell is empty
        if self.is_empty(position):
            self.board[position] = symbol
            return True
        else:
            return False

    def check_win(self, symbol):
        # check if the combination have the same symbol-->win
        win_list = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for win in win_list:
            if self.board[win[0]] == self.board[win[1]] == self.board[win[2]] == symbol:
                return True

        return False

    def is_full(self):
        # check if the board is full
        for cell in self.board:
            if cell == " ":
                return False
        return True


class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    def make_move(self, board):
        # get the move from the player
        # check if the move is valid,if it is invalid,ask the player to make another move
        while True:
            move = int(input(f"Movement for Symbol {self.symbol}: "))
            if board.is_empty(move):
                if 0 <= move <= 8:
                    return move
            else:
                print('Invalid move,please make another move:')


def main():
    # initiate the board and player
    p1 = Player('X')
    p2 = Player('O')
    current_player = p1
    game_board = Board()

    while True:
        # display the board and move one step
        game_board.draw()
        # move is set as the current position for set_chess
        move = current_player.make_move(game_board)

        # check the result of this move
        if game_board.set_chess(move, current_player.symbol):
            # when it is a valid move,check if the player wins or the game is a tie

            if game_board.check_win(current_player.symbol):
                game_board.draw()
                print(f'Player {current_player.symbol} wins !')
                break

            if game_board.is_full():
                game_board.draw()
                print('This game is a tie.')
                break

        # exchange the player
        if current_player == p1:
            current_player = p2
        else:
            current_player = p1


if __name__ == '__main__':
    main()
