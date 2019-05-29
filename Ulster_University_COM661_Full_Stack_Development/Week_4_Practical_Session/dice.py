import random

class Dice():

    def __init__(self):
        self.dice_one = 1
        self.dice_two = 1
        self.count = 0

    def roll(self):
        self.dice_one = random.randint(1, 6)
        self.dice_two = random.randint(1, 6)

    def get_roll(self):
        if self.dice_one == 1 and self.dice_two == 1:
            self.count += 1
            return "{} & {} - SNAKE EYES!".format(self.dice_one, self.dice_two)
        else:
            return "{} & {}".format(self.dice_one, self.dice_two)

    def get_count(self):
        return self.count
