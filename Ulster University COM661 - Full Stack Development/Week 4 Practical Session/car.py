class Car:

    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    def accelerate(self, speed_step):
        self.__speed += speed_step


    def brake(self, reduce_speed_step):
        self.__speed = self.__speed - reduce_speed_step


    def get_speed(self):
        return self.__speed
