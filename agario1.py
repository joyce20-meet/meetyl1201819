'''
import turtle
import time
import random
from ball import Ball
turtle.tracer(1)
turtle.hideturtle()
RUNNING = True
SLEEP = 0.0077
turtle.pu()
SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2
# My_Ball = Ball(100,100,5,4,20,"pink")
NUMBER_OF_BALLS = 5
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 100
MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5
MAXIMUM_BALL_DY = 5
MINIMUM_BALL_DY = -5
while True :
	My_Ball.move(SCREEN_WIDTH,SCREEN_HEIGHT)
BALLS = []
# def ball(self):
for i in range(NUMBER_OF_BALLS):
	x = random.randint(int(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS) , int(SCREEN_WIDTH - MAXIMUM_BALL_RADIUS))
	y = random.randint(int(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS) ,int(SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS))
	
	
	dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
	dy = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DY)
	radius = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
	# color = random.randint(random.random() , random.random())
	# self.random(x,y,dx,dy,radius.color)
	newball = Ball(x,y,dx,dy,radius)
	# random.randint()
	
	BALLS.append(newball)


def move_all_balls():
	for i in BALLS:
		i.move(SCREEN_WIDTH, SCREEN_HEIGHT) 
move_all_balls()

turtle.mainloop()
'''