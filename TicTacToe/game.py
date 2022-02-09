class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] #we will use a single list to represent a 3x3 board
        self.current_winner = None #track current winner

    def print_board(self):
        #this is getting the rows
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
    
    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 etc tells what number corresponds to what box
        number_board = [[str(i) for i in range(j*3, (j+1)*3) for j in range (3)]]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')
    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
        
        ## The entire for loop below is replaced by the single line above
        
        # moves = []
        # for (i, spot) in enumerate(self.board):
        #     # ['x', 'x', 'o'] --> [(0, 'x'), (1, 'x'), (2, 'o')]
        #     if spot == ' ':
        #         moves.append(i)
        # return moves
    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        # if valid move, then make the move (assign square to a letter)
        # then return true, if invalid, return false
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        #winner if 3 in a row anywhere. Must check all possibilities
        #first, check row
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind +1) * 3]
        if all([spot == letter for spot in row]):
            return True

        #second, check column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        #Finally, check diagonals
        # only needs to be done if square is an even number (0,2,4,6,8)
        # these are the only moves possible to win a diagonal
        


def play(game, x_player, o_player, print_game=True):
    #returns the winner of the game(by letter, either X or O) or None for Tie
    if print_game:
        game.print_board_nums()

    letter = 'X' #starting letter
    # iterate while the game still has empty squares
    # we don't have to worry about the winner because we'll just return that
    # which breaks the loop
    while game.empty_squares():
        #get move from appropriate player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        # let's define a function to make a move
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print('') #just empty line

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter

            #after move, we need to alternate letters
            letter = 'O' if letter == 'X' else 'X'

        if print_game:
            print('It\'s a tie!)