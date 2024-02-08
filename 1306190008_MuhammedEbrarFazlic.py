import random
from time import sleep

ROW_SIZE = 9
COLUMN_SIZE = 9
NUM_DISCS = 40
MAX_MOVES = 80
BOARD_FILE = "Tahta.txt"
MOVE_FILE = "Hamle.txt"
PLAYERS = ["Player 1", "Player 2"]
COLORS = ["R", "Y"]

class ConnFour:
    def __init__(self, row_size, column_size):
        self.rows = row_size
        self.columns = column_size
        self.board = [[' ' for _ in range(ROW_SIZE)] for _ in range(COLUMN_SIZE)]

    # Function to print the board
    def print_board(self):
        for i in range(1, 10):
            print(str(i).center(5), end='')
        print()
        for row in self.board:
            print(row)

    # Function to save the board state to a file
    def save_board(self):
        with open(BOARD_FILE, "w") as file:
            for row in self.board:
                file.write("".join(row) + "\n")
    
    # Function to retreive the board from file
    def retrieve_board(self):
        with open(BOARD_FILE, "r") as file:
            lines = file.readlines()
            for row in range(ROW_SIZE):
                try:
                    self.board[row] = list(lines[row].strip("\n"))
                except IndexError:
                    print("No saved games!")
                    sleep(2)
                    exit(1)


    # Function to save moves to a file
    def save_move(self, player, row, column):
        with open(MOVE_FILE, "a") as file:
            file.write(f"{player}: row:{row} column:{column}\n")

    def get_column(self, index):
        return [i[index] for i in self.board]

    # Function to make a move
    def make_move(self, player, column):
        if " " not in self.get_column(column):
            return self.board
        row = self.rows - 1
        while self.board[row][column] != " ":
            row -= 1
        self.board[row][column] = player
        self.save_move(player, row, column)
        self.save_board()

    # Function to check if a player has won
    def check_win(self, player):
        # Check rows
        for row in range(ROW_SIZE):
            for col in range(COLUMN_SIZE - 3):
                if self.board[row][col] == player and \
                self.board[row][col + 1] == player and \
                self.board[row][col + 2] == player and \
                self.board[row][col + 3] == player:
                    return True

        # Check columns
        for col in range(COLUMN_SIZE):
            for row in range(ROW_SIZE - 3):
                if self.board[row][col] == player and \
                self.board[row + 1][col] == player and \
                self.board[row + 2][col] == player and \
                self.board[row + 3][col] == player:
                    return True

        # Check diagonals bottom->top
        for row in range(ROW_SIZE - 3):
            for col in range(COLUMN_SIZE - 3):
                if self.board[row][col] == player and \
                self.board[row + 1][col + 1] == player and \
                self.board[row + 2][col + 2] == player and \
                self.board[row + 3][col + 3] == player:
                    return True

        # Check diagonals top->bottom
        for row in range(3, ROW_SIZE):
            for col in range(COLUMN_SIZE - 3):
                if self.board[row][col] == player and \
                self.board[row - 1][col + 1] == player and \
                self.board[row - 2][col + 2] == player and \
                self.board[row - 3][col + 3] == player:
                    return True
        return False

if __name__ == '__main__':
    #Giving players colors
    random.shuffle(COLORS)
    player_colors = dict(zip(PLAYERS, COLORS))
    
    #Starting the game
    inp = input("1- Start new game \n2- Continue saved game\n")
    if inp == "1":
        game = ConnFour(ROW_SIZE, COLUMN_SIZE)
        open(BOARD_FILE, 'w').close()
        open(MOVE_FILE, 'w').close()
    elif inp == "2":
        game = ConnFour(ROW_SIZE, COLUMN_SIZE)
        game.retrieve_board()
    else:
        print("Invalid input!")
        sleep(2)
        exit()

    turncount = 0
    while turncount <= 80:
        if turncount == 0:
            game.print_board()

        #Player 1 moves
        while True:
            try:
                col = int(input("Player 1, Choose column: \nTo save the board and exit, press 0\n")) - 1 
            except ValueError:
                print("Invalid input!")
                continue
            if col == -1:
                game.save_board()
                print("Game saved!")
                sleep(2)
                exit(1)
            else:
                break
        game.make_move(player_colors["Player 1"], col)
        #Check if Player 1 won
        game.print_board()
        if game.check_win(player_colors["Player 1"]):
            print("Player 1 has won!")
            break

        #Player 2 moves
        while True:
            try:
                col = int(input("Player 2, Choose column: \nTo save the board and exit, press 0\n")) - 1 
            except ValueError:
                print("Invalid input!")
                continue
            if col == -1:
                game.save_board()
                print("Game saved!")
                sleep(2)
                exit(1)
            else:
                break
        game.make_move(player_colors["Player 2"], col)
        #Check if Player 2 won
        game.print_board()
        if game.check_win(player_colors["Player 2"]):
            print("Player 2 has won!")
            break
        
        turncount += 1

    print("Thanks!")
    sleep(2)
    exit(1)