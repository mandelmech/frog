import random
import numpy as np

# This defines the class Frog, which will have the attribute position and the ability to move throughout a board
class Frog:
    # This is the position of the Frog
    pos = 0

    # This will define where the frog moves
    def move(self):
        newpos = random.randint(self.pos + 1, len(board) - 1)
        self.pos = newpos


# This creates a board of the size that we choose, here is where the frog will move.
def createboard(size):
    board = []
    for i in list(range(size + 1)):
        board.append(i)
    return board


# This defines the game, the frog will continually move until it reaches its final destination. Returns number of moves
def game(player):
    player.pos = 0
    nummoves = 0
    while True:
        player.move()
        nummoves += 1
        if player.pos == board[-1]:
            return nummoves


# This list defines which sizes of boards will be tried (i.e.) number of pads to leap or length of pond, can be changed
board_sizes = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# Create the frog!! :D
frog = Frog()

# Number of iterations
# The program will run as many times as defined by it on each of the sizes defined by board_sizes
it = int(input('Enter number of iterations: '))

# The program will also write the results to a file named log.txt
file = open('log.txt', 'a')
file.write('Iterations = {}\n'.format(it))

for size in board_sizes:
    results = []
    board = createboard(size)
    file.write('Board Size = {}\n'.format(size))
    count = 0
    while True:
        x = game(frog)
        results.append(x)
        count += 1
        if count == it:
            break
    average = np.average(results)
    file.write('Average moves = {}\n\n'.format(average))

file.close()

