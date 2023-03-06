import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car = CarManager()
player.create_turtle()
screen.listen()
screen.onkey(player.move_forward,"Up")
game_is_on = True
while game_is_on:
    car.create_cars()
    car.move()
    time.sleep(0.1)
    screen.update()
    for i in car.all_cars:
        if i.distance(player) < 20:
            game_is_on = False
    if player.is_at_finish():
        player.goto_start()
        car.level_up()

            
   


