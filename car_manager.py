from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 1


class CarManager:
    def __init__(self):
        self.cars = []
        self.create_car()
        self.cars_speed = STARTING_MOVE_DISTANCE
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
            car.backward(self.cars_speed)
            
    def next_stage(self):
        self.cars_speed += MOVE_INCREMENT
        self.reset_cars()
        
    def reset_cars(self):
        for car in self.cars:
            car.goto(1000,1000)   
        self.cars.clear()    
        
