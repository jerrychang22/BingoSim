import random
import numpy as np
import matplotlib.pyplot as plt

THROUGH_RANGE = 1
NUM_GAMES = 10000
NUM_PLAYERS = 25
BOARD_SIZE_X = 5
BOARD_SIZE_Y = 5
#Must be greater than 0. 
#Maybe I'll make 0 and negatives available in the future
#Would need to change the way checking for wins works to a seperate array set
START_RANGE = 1   
INTERVAL = 15
FREE_SPACE = True
END = START_RANGE + BOARD_SIZE_X * INTERVAL

def init_board(board_size_x, board_size_y, start, interval, free):
    board = []

    #Generate a column of numbers for each LETTER
    for x in range(board_size_x):
        s = start + x * interval
        l = random.sample(range(s, s + interval), board_size_y)
        
        #Add free space
        if free:
            if (2*x+1)/2 == board_size_x/2:
                l[board_size_y // 2] = 0
        board.append(l)

    
    return np.array(board, dtype=int)
   


def standard_win(board):
    #Check rows for 0's
    out = list(map(np.sum, board))
    if 0 in out:
        return 1

    #Check cols for 0's
    out = list(map(np.sum, board.T))
    if 0 in out:
        return 1

    #Check diagonals for 0's
    if board.trace() == 0:
        return 1
    if np.fliplr(board).trace() == 0:
        return 1
    
    else:
        return 0

def t_win(board):
    return 0

WIN_CONDITION = standard_win

def play_bingo(player_boards):
    win = False
    counter = 1

    while win == False:
        #Call a random number
        rand_call = random.randint(START_RANGE, END)
        #print("Turn " + str(counter) + " : " + str(rand_call) + " was called\n")
        counter += 1

        #Search all boards for called number
        for board in range(NUM_PLAYERS):
            for row in player_boards[board]:
                if rand_call in row:
                    #Replace number with 0 if found 
                    #print("Found " + str(rand_call) + " in Player " + str(board + 1) + "\n" + str(player_boards[board]) + "\n")
                    ind = row.tolist().index(rand_call)
                    row[ind] = 0



        #Check for wins
        check = list(map(WIN_CONDITION, player_boards))
        win = 1 in check

    winning_player = check.index(1) + 1
    #print("Winning player : Player " + str(winning_player) + "\n")
    return counter


def main():
    player_boards = []
    #print("Playing Bingo\n")
    
    data = []

    for players in range(NUM_PLAYERS, NUM_PLAYERS - THROUGH_RANGE, -1):
        
        turns = []
        for game in range(NUM_GAMES):

            for a in range(players):
                new_board = init_board(BOARD_SIZE_X, BOARD_SIZE_Y, START_RANGE, INTERVAL, FREE_SPACE)
                player_boards.append(new_board)
                
            turns.append( play_bingo(player_boards) )
            player_boards = []
        data.append(turns)

    #Plot data
    #print(data[0])
    plt.hist(data[0])
    plt.grid(True)
    plt.show()
    

    return 0;




main()
