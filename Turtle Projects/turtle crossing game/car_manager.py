from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self) :
        self.all_cars = []
        self.car_speed = MOVE_INCREMENT
        self.create_cars()
    def create_cars(self):
        num = random.randint(1,6)
        if num == 1:
             new_y = random.randint(-270,270)
             new_car = Turtle()
             new_car.penup()
             new_car.shape("square")
             new_car.shapesize(stretch_wid=1,stretch_len=2)
             new_car.color(random.choice(COLORS))
             new_car.goto(x=300,y=new_y)
             self.all_cars.append(new_car)
    def move (self):
        for item in self.all_cars:
            item.backward(self.car_speed)
    def level_up(self):
        self.car_speed += MOVE_INCREMENT



