import random


class The_Board:
    """
    prints out the games board
    """
    def __init__(self, board):
        self.board = board

    def get_letters_to_numbers():
        """
        converts letters in a list of numbers
        """
        letters_to_numbers = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5,
                              "G": 6, "H": 7}
        return letters_to_numbers

    def print_board(self):
        """
        creates 1 row then loops through the board
        (which will be 8 times) adding a pipe separator (|)
        """
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
        """
        creates the ships and positions them on the board
        """
        for i in range(5):
            # get the row and column then randomize the ships location
            self.x_row, self.y_column = random.randint(0, 7), random.randint(0, 7)
            # checks if a ship has already been placed there.
            # If so will rerandomize
            while self.board[self.x_row][self.y_column] == "X":
                self.x_row, self.y_column = random.randint(0, 7), random.randint(0, 7)
            self.board[self.x_row][self.y_column] = "X"
        return self.board

    def The_user_input(self):
        """
        The functions get user input (row number and column letter)
        """
        try:
            x_row = input("Enter the row  of the ship:\n ")
            # checks for numbers 1 - 8
            while x_row not in '12345678':
                # If invalid will print:
                print('inappropriate choice, please select a valid row')
                # Then ask for x_row input again
                x_row = input('Enter  the row  of the ships:\n ')

            y_column = input("Enter the column letter of the ship: ").upper()
            # checks for letters A - H
            while y_column not in "ABCDEFGH":
                # If invalid will print:
                print('inappropriate choice, please select a valid column')
                # Then ask for y_column input again
                y_column = input("Enter the column letter of the ships:\n"
                                 ).upper()
            return int(x_row) - 1, The_Board.get_letters_to_numbers()[y_column]
        except ValueError and KeyError:
            print("Not a valid  input")
            return self.The_user_input()

    def ship_hit_count(self):
        """
        This fuction looks for "X" on the board
        """
        hit_ships = 0
        # Loops through The_Board
        for row in self.board:
            # Then loops through column and row
            for column in row:
                if column == "X":
                    # if "X" found adds 1 to hit count
                    hit_ships += 1
        return hit_ships


def RunGame():
    """
    This is the main function that runs the game by calling all other fuctions
    """
    print("-" * 57)
    print("Welcome to Sink That Ship.")
    print("To win the game you have to sink the computers 5 ships.")
    print("You have 10 turns to do so.")
    print("-" * 57)
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
