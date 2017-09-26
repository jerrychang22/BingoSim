import random
import numpy as np

def main():
    board = init_board(5,5,1,15,False)
    print(board)
    return 0;


def init_board(board_size_x, board_size_y, start, interval, free):
    board = []

    #Generate a column of numbers for each LETTER
    for x in range(0, board_size_x):
        s = start + x * interval
        l = random.sample(range(s, s + interval), board_size_y)
        board.append(l)

    return board
        
main()
