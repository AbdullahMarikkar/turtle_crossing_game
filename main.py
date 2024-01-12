import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()

screen.listen()
screen.onkey(player.go_up,"w")
screen.onkey(player.go_down,"s")




game_is_on = True
while game_is_on:
    
            
    time.sleep(0.1)
    screen.update()
    
    car_manager.create_car()
    car_manager.move_cars()
    
    
    #Detect collision with car
    for car in car_manager.cars:
        if (car.distance(player)<25):
            game_is_on = False
    
    if(player.ycor()>280):
        player.restart()
        car_manager.next_stage()





screen.exitonclick()