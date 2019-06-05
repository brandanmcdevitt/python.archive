import sys
import math

# The while loop represents the game.
# Each iteration represents a turn of the game
# where you are given inputs (the heights of the mountains)
# and where you have to print an output (the index of the mountain to fire on)
# The inputs you are given are automatically updated according to your last actions.

# game loop
while True:
    h = []
    for i in xrange(8):
        mountain_h = int(raw_input())  # represents the height of one mountain.
        h.append(mountain_h)
    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."

    # The index of the mountain to fire on
    index = [i for i, x in enumerate(h) if x == max(h)]
    print(index[0])