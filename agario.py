
import turtle
import time
import random
from ball import Ball
import math
turtle.tracer(0,0)
turtle.hideturtle()
RUNNING = True
SLEEP = 0.0077
turtle.pu()
SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2
MY_BALL = Ball(0,0,5,4,70,"pink")
NUMBER_OF_BALLS = 5
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 100
MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5
MAXIMUM_BALL_DY = 5
MINIMUM_BALL_DY = -5
global score
score = 0 
BALLS = []
for i in range(5):
	x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS , SCREEN_WIDTH - MINIMUM_BALL_RADIUS)
	while x in range (-MY_BALL.radius+MY_BALL.xcor(), MY_BALL.xcor()+MY_BALL.radius):
		x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS , SCREEN_WIDTH - MINIMUM_BALL_RADIUS)
	y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS , SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
	while y in range(-MY_BALL.radius + MY_BALL.ycor() , MY_BALL.ycor()+ MY_BALL.radius):
		y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS , SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
	dx = 0
	dy = 0
	while dx == 0:
		dx = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
	while dy == 0:
		dy = random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
	radius = random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
	color = (random.random(), random.random(), random.random())
	newballs = Ball(x,y,dx,dy,radius,color)
	BALLS.append(newballs)


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
				
				while x in range (int(-MY_BALL.radius+MY_BALL.xcor()), int(MY_BALL.xcor()+MY_BALL.radius)):
					x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS , SCREEN_WIDTH - MINIMUM_BALL_RADIUS)
	
				while y in range (int(-MY_BALL.radius+MY_BALL.ycor()), int(MY_BALL.ycor()+MY_BALL.radius)):
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
					ball_b.shapesize(ball_b.radius/10)
				else:
					ball_b.goto(x,y)
					ball_b.radius = radius
					ball_b.shapesize(radius/10)
					ball_b.color(color)
					ball_b.dx = dx
					ball_b.dy = dy 
					ball_a.radius = ball_a.radius + 1
					ball_a.shapesize(ball_a.radius/10)
def move_All_BALLS():
	for newballs in BALLS:
		newballs.move(SCREEN_WIDTH,SCREEN_HEIGHT)
def check_myball_collision():
	global score
	for ball in BALLS:
		if collide(MY_BALL,ball):
			MY_BALL_RADIUS = MY_BALL.radius
			ballRadius = ball.radius
			radius = random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)

			x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS , SCREEN_WIDTH - MINIMUM_BALL_RADIUS)
			y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS , SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
			while x in range (int(-MY_BALL.radius+MY_BALL.xcor()), int(MY_BALL.xcor()+MY_BALL.radius)):
					x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS , SCREEN_WIDTH - MINIMUM_BALL_RADIUS)
	
			while y in range (int(-MY_BALL.radius+MY_BALL.ycor()), int(MY_BALL.ycor()+MY_BALL.radius)):
					y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS , SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
			dx = 0
			dy = 0
			while dx == 0:
				dx = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
			while dy == 0:
				dy = random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
			color = (random.random(), random.random(), random.random())
			if MY_BALL_RADIUS < ballRadius: 
				# break
				return False
			if MY_BALL_RADIUS > ballRadius:
				MY_BALL.radius = MY_BALL.radius + 1
				MY_BALL.shapesize (MY_BALL.radius/10)
				ball.goto(x,y)
				ball.radius = radius
				ball.shapesize(radius/10)
				ball.color(color)
				ball.dx = dx
				ball.dy = dy 
				score = score+1
			turtle.undo()
			turtle.write(str(score),move=False , align="right" , font=("Arial",16,"bold"))
	return True
def movearound(event):
	x = event.x - SCREEN_WIDTH
	y = -event.y + SCREEN_HEIGHT
	MY_BALL.goto(x,y)

turtle.getcanvas().bind("<Motion>", movearound)
turtle.listen()
check_all_balls_collision()
check_myball_collision()
turtle.write(str(score))
while RUNNING:				
	RUNNING = check_myball_collision()
	move_All_BALLS()
	check_all_balls_collision()
	turtle.update()
	time.sleep(SLEEP)
turtle.write("You Lost",move=False , align='center' ,font=('Arial',16,"bold"))
turtle.mainloop()