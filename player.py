import turtle
from turtle import*
import random
import math
import time




SQUARE_SIZE = 20
UP_ARROW = "Up" 
LEFT_ARROW = "Left" 
RIGHT_ARROW = "Right"
SPACEBAR = "space"
ENTER = "return"

UP = 0
LEFT=1
DOWN=2
RIGHT=3



global direction
direction = UP
plat_colide = False
UP_EDGE = 250
DOWN_EDGE = -250
RIGHT_EDGE = 400
LEFT_EDGE = -400


def platform_colide():
	global plat_colide
	plat_colide = True

def platform_not_colide():
	global plat_colide
	plat_colide = False

def up():
	global direction
	direction = UP
	
def left():
	global direction
	if not direction == RIGHT:
		direction = LEFT



def right():
	global direction
	if not direction == LEFT:
		direction = RIGHT

# func = partial(up, running)
# turtle.onkeypress(up, UP_ARROW) 
turtle.onkeypress(left,LEFT_ARROW)

turtle.onkeypress(right,RIGHT_ARROW)
turtle.listen()


class Player(Turtle):
	def __init__(self, x, y,dx,dy):
		Turtle.__init__(self)
		self.pu()
		turtle.ht()
		self.goto(x,y)
		self.dx = dx
		self.dy = dy
		self.shape("square")
		self.shapesize(50/10)
		oldx = self.xcor()
		oldy = self.ycor()
		newx = oldx - 0.05
		newy = oldy - 0.05
		self.goto(newx,newy)
		self.height = 50
		self.width= 125
	def move_player(self,width,height):
		x_pos = self.xcor()
		y_pos = self.ycor()
		old_x = self.xcor()
		old_y = self.ycor()
		new_x = old_x - 0.05
		new_y = old_y - 0.05
		self.goto(new_x,new_y)



		global direction
		if direction==RIGHT:
			self.goto(x_pos + self.dx , y_pos)
			#print("You moved right!")
		elif direction==LEFT:
			self.goto(x_pos - self.dx , y_pos)
			#print("You moved left!")
		elif direction==UP and plat_colide:
			self.goto(x_pos , y_pos + self.dy)
			#print("You moved up")
			#print("You moved down")
		old_x = self.xcor()
		old_y = self.ycor()
		new_x = old_x + self.dx
		new_y = old_y + self.dy
	'''
	def falling_down(self):
		old_x = self.xcor()
		old_y = self.ycor()
		new_y = max(old_x, old_y - 1)
		self.goto(old_x,new_y)
	'''
'''
		if new_x >= width:
			direction=LEFT
		if new_x <= -width:
			direction = RIGHT 
		if new_y >= height:
			direction = DOWN
		if new_y <= -height:
			direction = UP
'''


	

	
