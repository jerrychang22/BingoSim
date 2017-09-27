import random
import numpy as np
#import matplotlib.pyplot as plt

NUM_PLAYERS = 1
BOARD_SIZE_X = 5
BOARD_SIZE_Y = 5
#Must be greater than 0. 
#Maybe I'll make 0 and negatives available in the future
#Would need to change the way checking for wins works to a seperate array set
START_RANGE = 1   
INTERVAL = 15
FREE_SPACE = False
END = START_RANGE + BOARD_SIZE_X * INTERVAL

def init_board(board_size_x, board_size_y, start, interval, free):
    board = []

    #Generate a column of numbers for each LETTER
    for x in range(0, board_size_x):
        s = start + x * interval
        l = random.sample(range(s, s + interval), board_size_y)
        board.append(l)

    
    return np.array(board, dtype=int)
   


def standard_win(board):
    #Check rows for 0's
    out = map(np.sum, board)
    if 0 in out:
        return 1

    #Check cols for 0's
    out = map(np.sum, board.T)
    if 0 in out:
        return 1

    #Check diagonals for 0's
    if np.sum(board.diagonal()) == 0:
        return 1
    if np.sum(board.diagonal(axis1 = 1, axis2 = 0)) == 0:
        return 1
    
    else:
        return 0

def t_win(board):
    return 0

WIN_CONDITION = standard_win

def play_bingo(player_boards):
    win = False

    while win == False:
        #Call a random number
        rand_call = random.randint(START_RANGE, END)
        
        #Search all boards for called number
        for board in player_boards:
            for row in board:
                if rand_call in row:
                    #Replace number with 0 if found 
                    print("Found " + str(rand_call) + " in \n" + str(board) + "\n")
                    ind = row.tolist().index(rand_call)
                    row[ind] = 0



        #Check for wins
        check = map(WIN_CONDITION, player_boards)
        win = 1 in check

def main():
    player_boards = []
    #status_boards = []
    for a in range(NUM_PLAYERS):
        new_board = init_board(BOARD_SIZE_X, BOARD_SIZE_Y, START_RANGE, INTERVAL, FREE_SPACE)
        player_boards.append(new_board)
        #new_status = [[0 for col in range(BOARD_SIZE_Y)] for row in range(BOARD_SIZE_X)]
        #status_boards.append(new_status)
    #print(player_boards)
    #print(status_boards)

    print("Playing Bingo\n")
    play_bingo(player_boards)
    return 0;




main()
