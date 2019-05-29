# day03: Intro To Conditional Statements

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())

# If N is odd, print Weird
if N % 2 == 1:
    print("Weird")
# If N is even and in the inclusive range of 2 to 5, print Not Weird
elif N % 2 == 0 and N in range(2, 6):
    print("Not Weird")
# If N is even and in the inclusive range of 6 to 20, print Weird
elif N % 2 == 0 and N in range(6, 21):
    print("Weird")
# If N is even and greater than 20, print Not Weird
elif N % 2 == 0 and N > 20:
    print("Not Weird")