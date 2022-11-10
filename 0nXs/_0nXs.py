#Classes

class OnXs:
    def __init__(self, player_1, player_2):
        
        self.game_board = [
                           [" "," "," "],
                           [" "," "," "],
                           [" "," "," "]
                           ]
        self.player_1 = player_1
        self.player_2 = player_2
        self.game_won = False
        
        self.print_game_board()

    def intro_screen():
        print("Lets play naughts and crosses!")
        print("\n")
        print(f" X | X | 0 ")
        print("-----------")
        print(f" X | 0 | O ")
        print("-----------")
        print(f" 0 | O | X ")
        print("\n")

    def print_game_board(self):
        print("\n")
        print("    [1] [2] [3]")
        print(f" [A] {self.game_board[0][0]} | {self.game_board[0][1]} | {self.game_board[0][2]} ")
        print("    -----------")
        print(f" [B] {self.game_board[1][0]} | {self.game_board[1][1]} | {self.game_board[1][2]} ")
        print("    -----------")
        print(f" [C] {self.game_board[2][0]} | {self.game_board[2][1]} | {self.game_board[2][2]}")
        print("\n")

    def make_move(self, player):
        valid_move = False
        while not valid_move:
            move = player.choose_move(player.name)
            valid_move = self.check_valid_move(move)
            if valid_move:
                self.update_game_board(move, player.playing_piece)
            else:
                print("Space taken. Try again: ")

    def check_valid_move(self, move):
        if move == "A1":
            if self.game_board[0][0] == " ":
                return True
            else:
                return False
        elif move == "A2":
            if self.game_board[0][1] == " ":
                return True
            else:
                return False
        elif move == "A3":
            if self.game_board[0][2] == " ":
                return True
            else:
                return False
        elif move == "B1":
            if self.game_board[1][0] == " ":
                return True
            else:
                return False
        elif move == "B2":
            if self.game_board[1][1] == " ":
                return True
            else:
                return False
        elif move == "B3":
            if self.game_board[1][2] == " ":
                return True
            else:
                return False
        elif move == "C1":
            if self.game_board[2][0] == " ":
                return True
            else:
                return False
        elif move == "C2":
            if self.game_board[2][1] == " ":
                return True
            else:
                return False
        elif move == "C3":
            if self.game_board[2][2] == " ":
                return True
            else:
                return False

    def update_game_board(self, move, playing_piece):
         if move == "A1":
            self.game_board[0][0] = playing_piece
         if move == "A2":
            self.game_board[0][1] = playing_piece
         if move == "A3":
            self.game_board[0][2] = playing_piece
         if move == "B1":
            self.game_board[1][0] = playing_piece
         if move == "B2":
            self.game_board[1][1] = playing_piece
         if move == "B3":
            self.game_board[1][2] = playing_piece
         if move == "C1":
            self.game_board[2][0] = playing_piece
         if move == "C2":
            self.game_board[2][1] = playing_piece
         if move == "C3":
            self.game_board[2][2] = playing_piece

    def check_for_win(self):
        if (self.game_board[0][0] != " " and 
            self.game_board[0][0] == self.game_board[0][1] == self.game_board[0][2]):
            return True
        if (self.game_board[1][0] != " " and 
            self.game_board[1][0] == self.game_board[1][1] == self.game_board[1][2]):
            return True
        if (self.game_board[2][0] != " " and 
            self.game_board[2][0] == self.game_board[2][1] == self.game_board[2][2]):
            return True
        if (self.game_board[0][0] != " " and 
            self.game_board[0][0] == self.game_board[1][1] == self.game_board[2][2]):
            return True
        if (self.game_board[0][2] != " " and 
            self.game_board[0][2] == self.game_board[1][1] == self.game_board[2][0]):
            return True
        if (self.game_board[0][0] != " " and 
            self.game_board[0][0] == self.game_board[1][0] == self.game_board[2][0]):
            return True
        if (self.game_board[0][1] != " " and 
            self.game_board[0][1] == self.game_board[1][1] == self.game_board[2][1]):
            return True
        if (self.game_board[0][2] != " " and 
            self.game_board[0][2] == self.game_board[1][2] == self.game_board[2][2]):
            return True

    def win_routine(self, player):
        self.game_won = True
        player.wins += 1
        print("\n")
        print("****************************")
        print("\n")
        print(f"{player.name} has won the game!")
        print("\n")
        print("****************************")
        print("\n")

    def __repr__(self):
        msg = "\"Tic-tac-toe, noughts and crosses, or Xs and Os is a paper-and-pencil game for two \
players who take turns marking the spaces in a three-by-three grid with X or O. The player who \
succeeds in placing three of their marks in a horizontal, vertical, or diagonal row is the winner.\" \
(Wikipedia Contributors, 2019) \nWikipedia Contributors (2019). Tic-tac-toe. [online] Wikipedia. \
Available at: https://en.wikipedia.org/wiki/Tic-tac-toe."
        return msg

class Player:
    def __init__(self):
        self.name = ""
        self.playing_piece = ""
        self.wins = 0

    def input_player_name(self):
        while not self.name:
            print("Please enter your name: ")
            self.name = input()

    def choose_move(self, name):
        self.move = ""
        self.valid_moves = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
        print(f"{name} make your move!")
        while self.move not in self.valid_moves:
            print("Please enter a valid column/row reference: ")
            self.move = input().upper()
        return self.move


#Main

play_again = True

OnXs.intro_screen()

print("Player 1 will be \'Os\'")
player_1 = Player()
player_1.input_player_name()
player_1.playing_piece = 'O'

print("\n")
print("Player 2 will be \'Xs\'")
player_2 = Player()
player_2.input_player_name()
player_2.playing_piece = 'X'

print("\n")
print("Let's play!")

while play_again:
    print("\n")
    print(f"{player_1.name} has {player_1.wins} wins.")
    print(f"{player_2.name} has {player_2.wins} wins.")

    game = OnXs(player_1, player_2)

    while not game.game_won:
        game.make_move(player_1)

        game.print_game_board()
        if game.check_for_win():
            game.win_routine(player_1)
            continue

        game.make_move(player_2)

        game.print_game_board()
        if game.check_for_win():
            game.win_routine(player_2)
            continue

    print("\n")

    while True:
        print("Do you want to play again?")
        user_input = input()

        if user_input.lower() == 'y':
            play_again = True
            break

        elif user_input.lower() == 'n':
            play_again = False
            break


            



