import random


class The_Board:
    """
    prints out the games board
    """
    def __init__(self, board):
        self.board = board

    def get_letters_to_numbers():
        letters_to_numbers = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5,
                              "G": 6, "H": 7}
        return letters_to_numbers

    def print_board(self):
        print(" A B C D E F G H")
        print(" +-+-+-+-+-+-+-+")
        row_number = 1
        for row in self.board:
            print("%d|%s" % (row_number, "|".join(row)))
            row_number += 1


class The_Battleship:
    def __init__(self, board):
        self.board = board

    def create_ships(self):
        for i in range(5):
            self.x_row, self.y_column = random.randint(0, 7), random.randint(0, 7)
            while self.board[self.x_row][self.y_column] == "X":
                self.x_row, self.y_column = random.randint(0, 7), random.randint(0, 7)
            self.board[self.x_row][self.y_column] = "X"
        return self.board

    def The_user_input(self):
        try:
            x_row = input("Enter the row  of the ship: ")
            while x_row not in '12345678':
                print('inappropriate choice, please select a valid row')
                x_row = input('Enter  the row  of the ships: ')

            y_column = input("Enter the column letter of the ship: ").upper()
            while y_column not in "ABCDEFGH":
                print('inappropriate choice, please select a valid column')
                y_column = input("Enter the column letter of the ships:"
                                 ).upper()
            return int(x_row) - 1, The_Board.get_letters_to_numbers()[y_column]
        except ValueError and KeyError:
            print("Not a valid  input")
            return self.The_user_input()

    def ship_hit_count(self):
        hit_ships = 0
        for row in self.board:
            for column in row:
                if column == "X":
                    hit_ships += 1
        return hit_ships


def RunGame():
    computer_board = The_Board([[" "] * 8 for i in range(8)])
    user_guess_board = The_Board([[" "] * 8 for i in range(8)])
    The_Battleship.create_ships(computer_board)
    # 10 turns
    turns = 10
    while turns > 0:
        The_Board.print_board(user_guess_board)
        # The user input 
        user_x_row, user_y_column = The_Battleship.The_user_input(object)
        # check if duplicate guess
        while user_guess_board.board[user_x_row][user_y_column] == "-" or user_guess_board.board[user_x_row][user_y_column] == "X":
            print("You guessed that one already")
            user_x_row, user_y_column = The_Battleship.The_user_input(object)
        # checks for the hits and misses
        if computer_board.board[user_x_row][user_y_column] == "X":
            print("You sunk 1 of my Battleships!")
            user_guess_board.board[user_x_row][user_y_column] = "X"
        else:
            print("You missed my battleship!")
            user_guess_board.board[user_x_row][user_y_column] = "-"
        # ckecks if have won or lost
        if The_Battleship.ship_hit_count(user_guess_board) == 5:
            print("You hit all 5 battleships!")
            break
        else:
            turns -= 1
            print(f"you have {turns} turns remaining")
            if turns == 0:
                print("Sorry you ran out of turns")
                The_Board.print_board(user_guess_board)
                break


if __name__ == '__main__':
    RunGame() 
    