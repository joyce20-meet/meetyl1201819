
import turtle
import time
import random
from ball import Ball
import math
turtle.tracer(1)
turtle.hideturtle()
RUNNING = True
SLEEP = 0.0077
turtle.pu()
SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2
MY_BALL = Ball(100,100,5,4,20,"pink")
NUMBER_OF_BALLS = 5
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 100
MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5
MAXIMUM_BALL_DY = 5
MINIMUM_BALL_DY = -5
BALLS = []
for i in range(5):
	#BALL = True
	#while BALL == True:
	x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS , SCREEN_WIDTH - MINIMUM_BALL_RADIUS)
	y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS , SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
	dx = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
	dy = random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
	radius = random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
	color = (random.random(), random.random(), random.random())
	newballs = Ball(x,y,dx,dy,radius,color)
	BALLS.append(newballs)
print(newballs)


def collide(ball_a,ball_b):
	if (ball_a == ball_b):
		return False
	distancex = ball_a.xcor() - ball_b.xcor()
	distancey = ball_a.ycor()- ball_b.ycor()
	D = math.sqrt(math.pow(distancex,2) + math.pow(distancey,2))
	sum_radius = ball_a.radius + ball_b.radius
	if (D + 10 <= sum_radius):
		return True
	else:
		return False
def check_all_balls_collision():
	for ball_a in BALLS:
		for ball_b in BALLS:
			if collide(ball_b,ball_a):
				# save radius 

				radius = random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
				x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS , SCREEN_WIDTH - MINIMUM_BALL_RADIUS)
				y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS , SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
				color = (random.random(), random.random(), random.random())
				dx = 0 
				dy = 0
				while dx == 0 :
					dx = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)

				while dy == 0:
					dy = random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)

				if ball_a.radius < ball_b.radius :
					ball_a.goto(x,y)
					ball_a.radius = radius
					ball_a.shapesize(radius/10)
					ball_a.color(color)
					ball_a.dx = dx
					ball_a.dy = dy 
					ball_b.radius = ball_b.radius + 1
				else:
					ball_b.goto(x,y)
					ball_b.radius = radius
					ball_b.shapesize(radius/10)
					ball_b.color(color)
					ball_b.dx = dx
					ball_b.dy = dy 
					ball_a.radius = ball_a.radius + 1
def move_All_BALLS():
	while 1==1:
		for newballs in BALLS:
			newballs.move(SCREEN_WIDTH,SCREEN_HEIGHT)
			check_all_balls_collision()

move_All_BALLS()
turtle.mainloop()