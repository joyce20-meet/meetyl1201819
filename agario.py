
from ball import Ball
import turtle
import time
import random
import math
import tkinter as tk
from tkinter import simpledialog
from turtle import Screen
turtle.tracer(0,0)
turtle.hideturtle()
RUNNING = True
SLEEP = 0.0077
turtle.pu()
SCREEN_WIDTH = turtle.getcanvas().winfo_width()//2
SCREEN_HEIGHT = turtle.getcanvas().winfo_height()//2
MY_BALL = Ball(0,0,10,10,30,"plum")
lives=3

#food
MINIMUM_FOOD_RADIUS = 5
MAXIMUM_FOOD_RADIUS = 10

#Main Variables
NUMBER_OF_BALLS = 7
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 100
MINIMUM_BALL_DX = -3
MAXIMUM_BALL_DX = 3.5
MAXIMUM_BALL_DY = 3.5
MINIMUM_BALL_DY = -3

#set up for the score
global score
score = 0 
Height = 350
Width = 40 
turtle.goto(Width,Height)

#setting my background color
turtle.register_shape('marble.gif')
turtle.bgpic('marble.gif')

greeting = simpledialog.askstring("Input", "Are you ready to start the game?(yes or no) ", parent=tk.Tk().withdraw())
if greeting == ("no") or greeting == ("No"):
	quit()

#time 
global timescore
timescore = 0
timewrite = turtle.Turtle()
timewrite.ht()
def timer():
	global timescore
	timescore = int(time.clock()*2.5)
	timewrite.goto(200,350)
	timewrite.clear()
	timewrite.write(" Time : " + str(timescore),move=False , align="left" , font=("Arial",16,"bold"))

# lists to store all of my balls so i can use them later
BALLS = []
FOOD = []
global Hearts
Hearts = []

#main collision function
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

#creating food
turtle.register_shape("pineapple.gif")
turtle.register_shape("heart.gif")

def create_heart():

    radius = 10
    heart1 = Ball(-200,350,0,0,radius,color)
    heart2 = Ball(-250,350,0,0,radius,color)
    heart3 = Ball(-300,350,0,0,radius,color)
    heart1.shape('heart.gif')
    heart2.shape("heart.gif")
    heart3.shape("heart.gif")
    Hearts.append(heart1)
    Hearts.append(heart2)
    Hearts.append(heart3)     
def create_food():
	for p in range(20):
		x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS , SCREEN_WIDTH - MINIMUM_BALL_RADIUS)
		y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS , SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
		
		radius = random.randint(MINIMUM_FOOD_RADIUS,MAXIMUM_FOOD_RADIUS)
		dx = dy = 0
		food = Ball(x,y,dx,dy,radius,color)
		FOOD.append(food)
		food.shape("pineapple.gif")


def eat_food():
	global score
	for food in FOOD:
		if collide(MY_BALL,food):
			MY_BALL_RADIUS = MY_BALL.radius
			foodRadius = food.radius
			x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS , SCREEN_WIDTH - MINIMUM_BALL_RADIUS)
			y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS , SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)

			while x in range (int(-MY_BALL.radius+MY_BALL.xcor()), int(MY_BALL.xcor()+MY_BALL.radius)):
					x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS , SCREEN_WIDTH - MINIMUM_BALL_RADIUS)
	
			while y in range (int(-MY_BALL.radius+MY_BALL.ycor()), int(MY_BALL.ycor()+MY_BALL.radius)):
					y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS , SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
			dx = 0
			dy = 0
			while dx == 0:
				dx = random.uniform(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
			while dy == 0:
				dy = random.uniform(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
				MY_BALL.radius = MY_BALL.radius + 1
				MY_BALL.shapesize (MY_BALL.radius/10)
				food.goto(x,y) 
				food.dx = dx
				food.dy = dy 
				score = score + 1
				turtle.undo()
				turtle.update()
				turtle.goto(Width,Height)
				turtle.write(str(score),move=False , align="right" , font=("Arial",16,"bold"))
	return True

#creating balls (Food for MY_BALL):
for i in range(7):
	x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS , SCREEN_WIDTH - MINIMUM_BALL_RADIUS)
	while x in range ((-MAXIMUM_BALL_RADIUS*3)+MY_BALL.xcor(), MY_BALL.xcor()+(MAXIMUM_BALL_RADIUS*3)):
		x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS , SCREEN_WIDTH - MINIMUM_BALL_RADIUS)
	y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS , SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
	while y in range((-MAXIMUM_BALL_RADIUS*3) + MY_BALL.ycor() , MY_BALL.ycor()+(MAXIMUM_BALL_RADIUS*3)):
		y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS , SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
	dx = 0
	dy = 0
	while dx == 0:
		dx = random.uniform(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
	while dy == 0:
		dy = random.uniform(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
	radius = random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
	color = (random.random(), random.random(), random.random())
	newballs = Ball(x,y,dx,dy,radius,color)
	BALLS.append(newballs)


def check_all_balls_collision():
	for ball_a in BALLS:
		for ball_b in BALLS:
			if collide(ball_b,ball_a):
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
					dx = random.uniform(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)

				while dy == 0:
					dy = random.uniform(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)

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
	global Hearts
	global lives
	for ball in BALLS:
		if collide(MY_BALL,ball):
			MY_BALL_RADIUS = MY_BALL.radius
			ballRadius = ball.radius
			radius = random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
			color = (random.random(), random.random(), random.random())
			x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS , SCREEN_WIDTH - MINIMUM_BALL_RADIUS)
			y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS , SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)

			while x in range (int(-MY_BALL.radius+MY_BALL.xcor()), int(MY_BALL.xcor()+MY_BALL.radius)):
					x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS , SCREEN_WIDTH - MINIMUM_BALL_RADIUS)
	
			while y in range (int(-MY_BALL.radius+MY_BALL.ycor()), int(MY_BALL.ycor()+MY_BALL.radius)):
					y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS , SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
			dx = 0
			dy = 0
			while dx == 0:
				dx = random.uniform(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
			while dy == 0:
				dy = random.uniform(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
			
			if MY_BALL_RADIUS < ballRadius:
				lives= lives -1
				ball.goto(x,y)
				ball.radius = radius
				ball.shapesize(radius/10)
				ball.color(color)
				ball.dx = dx
				ball.dy = dy 
				if lives == 2:
					Hearts[0].clear()
					Hearts[0].ht()
					turtle.update()
					print('You lost your heart')
				if lives == 1:
					Hearts[1].clear()
					Hearts[1].ht()
					turtle.update()
					print('You lost another heart')
				if lives == 0:
					Hearts[2].clear()
					Hearts[2].ht()
					turtle.update()
					print('Your last chance')
				return True
				
			else:
				if ballRadius > 30:
				
					MY_BALL.radius = MY_BALL.radius + 4
				if ballRadius < 30:
					MY_BALL.radius = MY_BALL.radius + 2
				MY_BALL.shapesize (MY_BALL.radius/10)
				ball.goto(x,y)
				ball.radius = radius
				ball.shapesize(radius/10)
				ball.color(color)
				ball.dx = dx
				ball.dy = dy 
				if ballRadius > 30:
					score = score + 3
				if ballRadius < 30:
					score = score +2
			turtle.undo()
			turtle.update()
			turtle.goto(Width,Height)
			turtle.write(str(score),move=False , align="right" , font=("Arial",16,"bold"))
	return True

def movearound(event):
	x = event.x - SCREEN_WIDTH
	y = -event.y + SCREEN_HEIGHT
	MY_BALL.move(SCREEN_WIDTH,SCREEN_HEIGHT)
	MY_BALL.goto(x,y)

turtle.getcanvas().bind("<Motion>", movearound)
turtle.listen()

def check():
	check_all_balls_collision()
	check_myball_collision()

	if MY_BALL.xcor() == newballs.xcor() or MY_BALL.ycor()==newballs.ycor():
		x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS , SCREEN_WIDTH - MINIMUM_BALL_RADIUS)
		y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS , SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)

def win():
	
	if score == 50:
		MY_BALL.color("gold")
		
turtle.write(str(score))
create_food()
create_heart()
#running all of the functions
while lives > 0:
	SCREEN_WIDTH = turtle.getcanvas().winfo_width()//2
	SCREEN_HEIGHT = turtle.getcanvas().winfo_height()//2
	check()				
	RUNNING = check_myball_collision()
	move_All_BALLS()
	check_all_balls_collision()
	turtle.update()
	time.sleep(SLEEP)
	win()
	eat_food()
	timer()
for ball in BALLS:
	ball.ht()
for food in FOOD:
	food.ht()

turtle.update()
MY_BALL.goto(50,100)
turtle.goto(0,0)
turtle.write("You Lost",move=False , align='center' ,font=('Arial',23,"bold"))
turtle.pu()
turtle.update()
turtle.goto(0,-50)
turtle.write(int(score),align = "center", font=("Arial",23,"bold"))
turtle.mainloop()

