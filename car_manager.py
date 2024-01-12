from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.create_car()
        self.game_on = True
        
        
    def create_car(self):
        random_chance = random.randint(1,6)
        if(random_chance == 1):
            car = Turtle("square")
            car.shapesize(stretch_wid=1,stretch_len=2)
            car.penup()
            car.color(random.choice(COLORS))
            car.goto(300,random.randint(-300,300))
            self.cars.append(car)
        
        
    def move_cars(self):    
        for car in self.cars:
            car.backward(STARTING_MOVE_DISTANCE)
