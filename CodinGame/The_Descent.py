import sys
import math

# The while loop represents the game.
# Each iteration represents a turn of the game
# where you are given inputs (the heights of the mountains)
# and where you have to print an output (the index of the mountain to fire on)
# The inputs you are given are automatically updated according to your last actions.

# game loop
while True:
    all_heights = []
    max_height = 0
    target = 0
    
    for i in xrange(8):
        mountain_h = int(raw_input())  # represents the height of one mountain.
        all_heights.append(mountain_h)
        
    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."
    
    for height in range(8):
        if all_heights[height] > max_height:
            max_height = all_heights[height]
            target = height


    # The index of the mountain to fire on.
    print(target)