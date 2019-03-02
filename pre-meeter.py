import turtle
from turtle import*
import random
import math
import time
from platform import Platform
from player import *
import tkinter as tk
from functools import partial

turtle.setup(1200,800)
turtle.tracer(0,0)
turtle.hideturtle()
running= True
SLEEP = 0.0077	
turtle.pu()
SCREEN_WIDTH = turtle.getcanvas().winfo_width()//3
SCREEN_HEIGHT = turtle.getcanvas().winfo_height()//3

number_of_platforms= 5
PLATFORMS = []
HEIGHTS = [-350,150,-50,-250,-450]
WIDTH = [-500,150,0,-150,-300,-450]
turtle.register_shape("meetlogo.gif")

'''
def randomize_platform():

	x=random.uniform(width/2-screen_width, screen_width-width/2)
	y=screen_height
'''

for i in range(5):
	x = WIDTH[i]
	y = HEIGHTS [i]
	while y == 210:
		y = random.randint(-200,200)
	new_platforms = Platform(x,y,width,shape,1.5,1.5,SCREEN_WIDTH)
	PLATFORMS.append(new_platforms)

def move_platforms_down():
	for new_platforms in PLATFORMS:
		new_platforms.move()


My_Player = Player(0,-340,0.5,0.5)

platform_height= 7
platform_width=3
player_height=50
player_width=125

def collide(platform):
	player_bottom= My_Player.ycor() - player_height
	player_top= My_Player.ycor() + player_height                      
	player_right= My_Player.xcor() + player_width          
	player_left= My_Player.xcor() -player_width


	platform_bottom= platform.ycor()-platform_height
	platform_top= platform.ycor()+platform_height
	platform_right= platfogrm.xcor()+platform_width
	platform_left= platform.xcor()- platform_width

	if platform_top>= player_bottom and platform_bottom<=player_top and platform_right>=player_left and platform_left<=player_right:
		return True
	return False

turtle.update()
global timescore
timescore = 0
timewrite = turtle.Turtle()
timewrite.ht()

def timer():
	global timescore
	timescore = int(time.clock()*2.5)
	timewrite.goto(-500,350)
	timewrite.clear()
	timewrite.write(" Time : " + str(timescore),move=False , align="left" , font=("Arial",16,"bold"))
'''def collide(platfrom_a,platform_b):
	if platfom_a.top() >= platfrom_b.bottom():
		if platfrom_a.right() >= platfrom_b.left():
			if platfrom_a.bottom() <= platform_b.top()
				if platfrom_a.left() <= platform_b.right():
					turtle.goto

def check_player_collision():
	for platfrom in PLATFORMS:
		if collide(My_Player,PLATFORMS):
			if My_Player.ycor() == PLATFORMS.ycor():
				y_pos = My_Player.ycor() + 5 
				My_Player.goto(y_pos)
			turtle.update()

'''
# running=False
# func = partial(up, running)

# turtle.onkeypress(func, UP_ARROW) 
turtle.listen()
while True:
	move_platforms_down()
	running = False
	for platform in PLATFORMS:
		running = collide(platform)
	My_Player.move_player(-100,100)
	if running == False:
		#My_Player.falling_down()
		platform_not_colide()
	else:
		platform_colide()

	
	

	turtle.update()
	timer()

turtle.mainloop()
