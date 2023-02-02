import matplotlib.pyplot as plt
import numpy as np
import argparse
import matplotlib.animation as animation
from time import sleep
#set up parser
parser = argparse.ArgumentParser(
                    prog = "Conway's game of life",
                    description = "creates a 2D board of square cells where cells live and die due to conway's game of life",
                    epilog = 'if size is not specified default size is 20')
parser.add_argument(
    "--size", "-s",
    type=int, default=20, 
    dest="size", 
    help="number of rows and columns to create per square cells")
args = parser.parse_args()


# set up figure and ax
fig = plt.figure()
ax = fig.add_subplot(1,1,1)

#set up initial value
board = np.random.randint(2, size=(args.size, args.size))

#write a function to update cells on the board
def update_cells():
    global board
    pass

#write a function to update the board
def update_board(i):
    global board
    print(i)
    board = np.random.randint(2, size=(args.size, args.size))
    ax.clear()
    ax.matshow(board)
    

ani = animation.FuncAnimation(fig, update_board, interval=1000)
plt.show()