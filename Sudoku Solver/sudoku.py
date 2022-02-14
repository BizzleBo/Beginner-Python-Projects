from pprint import pprint

#This project will solve a given sudoku puzzle

def find_next_empty(puzzle):
    #finds the next row, col on the puzzle that isnt filled yet
    #return row, col tuple (or None, None) if there is none
    for r in range(9):
        for c in range(9):
            if puzzle [r][c] == -1:
                return r, c

    return None, None #if no spaces are available

def is_valid(puzzle, guess, row, col):
    #return True if we have a valid guess, False if not
    row_vals = puzzle[row]
    if guess in row_vals:
        return False

    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range (col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False

    return True


def solve_sudoku(puzzle):
    #solve puzzle using backpacking technique
    #step 1: choose somewhere on the board to make a guess
    row, col = find_next_empty(puzzle)

    #step 1.1: if theres nowhere left, then we're done because we only allow valid inputs
    if row is None:
        return True

    #step 2: if there is a place for the guess, make a guess between 1 & 9
    for guess in range(1, 10):
        #step3: check if guess is valid
        if is_valid(puzzle, guess, row, col):
            #step 3.1: if valid, place that guess on the board
            puzzle[row][col] = guess
            #step 4: recursively call our function
            if solve_sudoku(puzzle):
                return True

        #step 5: if no valid OR if our guess does not solve,
        # then backtrack to try again
        puzzle[row][col] = -1 #reset the guess

    #step 6: if none of our guesses work, then this is unsolvable
    return False

if __name__ == '__main__':
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    print(solve_sudoku(example_board))
    pprint(example_board)
