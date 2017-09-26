import random
import numpy as np
#import matplotlib.pyplot as plt

NUM_PLAYERS = 1
BOARD_SIZE_X = 5
BOARD_SIZE_Y = 5
START_RANGE = 1     #Must be greater than 0. Maybe I'll make 0 and negatives available in the future
INTERVAL = 15
FREE_SPACE = False
END = START_RANGE + BOARD_SIZE_X * INTERVAL


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


def init_board(board_size_x, board_size_y, start, interval, free):
    board = []

    #Generate a column of numbers for each LETTER
    for x in range(0, board_size_x):
        s = start + x * interval
        l = random.sample(range(s, s + interval), board_size_y)
        board.append(l)

    return board
   

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
                    print("Found " + str(rand_call) + " in " + str(board))
                    ind = row.index(rand_call)
                    row[ind] = 0

        #Check for wins





main()
