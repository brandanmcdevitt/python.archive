# day 10: Binary Numbers

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    # strip any white space from input and conver to int
    n = int(input().strip())
    # convert to base 2 with bin and split any 0's, returning the highest length
    # list item
    print(max(len(length) for length in bin(n)[2:].split('0')))