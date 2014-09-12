from ucb import main

class Board:
    def __init__(self, n):
        self.n = n
        # Create an n by n board, with no pieces
        self.board = []
        for i in range(n):
            self.board.append([' '] * n)

    # A player_type is just the string 'X' or 'O'
    def play_move(self, player_type, column, row):
        assert player_type == 'X' or player_type == 'O'
        if self.board[row][column] == ' ':
            self.board[row][column] = player_type
            return True
        return False

    def is_full(self):
        for row in range(self.n):
            if ' ' in self.board[row]:
                return False
        return True

    def has_won(self, player_type):
        # Check for a winning row
        if [player_type] * self.n in self.board:
            return True

        # Check for a winning column
        for i in range(self.n):
            winning_column = True
            for j in range(self.n):
                if self.board[j][i] != player_type:
                    winning_column = False
            if winning_column:
                return True

        # Check for a winning diagonal
        winning_main_diagonal = True
        winning_off_diagonal = True
        for i in range(self.n):
            if self.board[i][i] != player_type:
                winning_main_diagonal = False
            if self.board[i][self.n - i - 1] != player_type:
                winning_off_diagonal = False
        return winning_main_diagonal or winning_off_diagonal

    # Pretty prints the board
    def __str__(self):
        separator = '  ' + ('|---' * self.n) + '|\n'
        result = '    ' + '   '.join([str(x) for x in range(self.n)]) + '\n'
        result += separator
        for i in range(self.n):
            result += str(i) + ' | ' + ' | '.join(self.board[i]) + ' |\n'
            result += separator
        return result

class Player:
    def __init__(self, name, board, player_type):
        self.name = name
        self.board = board
        self.player_type = player_type

    def make_move(self):
        # Loop forever until the user enters a valid move
        while True:
            move = input('Enter a move in the form "column row", ' + self.name + ': ')
            move = self.parse_move(move)
            if move:
                column, row = move
                if self.board.play_move(self.player_type, column, row):
                    # Only once we get a valid move do we stop the loop
                    return
            print('Invalid move')

    def parse_move(self, move):
        tokens = move.strip().split()
        if len(tokens) != 2:
            return False
        column, row = tokens
        try:
            column, row = int(column), int(row)
            if column in range(self.board.n) and row in range(self.board.n):
                return column, row
            return False
        except ValueError:
            return False

@main
def play_game(n=3):
    # Set up all of the objects
    board = Board(n)
    name1 = input('Enter your name, player 1: ')
    player1 = Player(name1, board, 'X')
    name2 = input('Enter your name, player 2: ')
    player2 = Player(name2, board, 'O')

    # Play the game
    # Players alternate turns
    # Game ends if someone wins or the board becomes full.
    curr_player, other_player = player1, player2
    while not board.is_full():
        print('Current board is:')
        print(board)
        curr_player.make_move()
        if board.has_won(curr_player.player_type):
            print(curr_player.name + ' wins!')
            print(board)
            return
        curr_player, other_player = other_player, curr_player

    # If we reach here, the board must be full.
    print('The game is a draw.')
    print(board)
