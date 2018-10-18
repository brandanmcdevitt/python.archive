from math import pi

class Circle:

    def __init__(self, radius, center_x, center_y):
        self.__radius = radius
        self.__center_x = center_x
        self.__center_y = center_y

    def area(self):
        return pi * self.__radius ** 2

    def circumference(self):
        return 2 * pi * self.__radius

    def top_point(self):
        return self.__center_y + self.__radius

    def right_point(self):
        return self.__center_x + self.__radius