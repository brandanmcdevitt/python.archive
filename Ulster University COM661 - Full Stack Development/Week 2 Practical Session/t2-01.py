import random

def toss_coin(n):
    heads = 0
    tails = 0

    for x in range(n):
        number = random.randint(0,1)

        if number == 0:
            tails += 1
        elif number == 1:
            heads += 1

    print("Heads: {}, Tails: {}".format(heads, tails))


toss_coin(10)