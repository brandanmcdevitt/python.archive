from circle import Circle
from car import Car
from dice import Dice

def calc_circle(r, x, y):

    circle = Circle(r, x, y)

    print("The circumference of a circle with a radius of {} at position {}, {} = {}".format(r, x, y, round(circle.circumference(), 2)))
    print("The area of a circle with a radius of {} at position {}, {} = {}".format(r, x, y, round(circle.area(), 2)))
    print("The top point of a circle with a radius of {} at position {}, {} = {}".format(r, x, y, circle.top_point()))
    print("The right point of a circle with a radius of {} at position {}, {} = {}".format(r, x, y, circle.right_point()))

radius = int(input("Please enter a radius: "))
center_x = int(input("Please enter coordinates for X position: "))
center_y = int(input("Please enter coordinates for Y position: "))

calc_circle(radius, center_x, center_y)


def calc_speed(y, m, a, b):

    car = Car(y, m)

    for i in range(0, 5):
        car.accelerate(a)
        print("Car accelerating at {}mph".format(a))

    print("Current speed of car: {}mph".format(car.get_speed()))

    for i in range(0, 5):
        car.brake(b)
        print("Car decelerating at {}mph".format(b))

    print("Current speed of car: {}mph".format(car.get_speed()))

model = raw_input("Please enter the model of the car: ")
make = raw_input("Please enter the make of the car: ")
accelerate = int(input("Please enter the speed to accelerate at: "))
brake = int(input("Please enter the speed to decelerate at: "))

calc_speed(model, make, accelerate, brake)

def roll_dice(r):

    dice = Dice()

    for i in range(1, r + 1):
        dice.roll()
        print("Loop {}: {}".format(i, dice.get_roll()))

    print("Snake eyes appeared {} times".format(dice.get_count()))

rolls = int(input("How many times would you like to roll the dice? "))

roll_dice(rolls)