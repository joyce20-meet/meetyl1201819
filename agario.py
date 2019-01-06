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
My_Ball = Ball(100,100,5,4,20,"pink")
NUMBER_OF_BALLS = 5
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 100
MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5
MAXIMUM_BALL_DY = 5
MINIMUM_BALL_DY = -5
while True :
	My_Ball.move(SCREEN_HEIGHT,SCREEN_WIDTH)
BALLS = []
for i in range(5):
	random.randint()
	x = (-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS , SCREEN_WIDTH - MINIMUM_BALL_RADIUS)
	y = (-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS , SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS) 
	dx = ( MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
	dy = (MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
	radius = (MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
	color = (random.random() , random.random())
	random.randint()
turtle.mainloop()