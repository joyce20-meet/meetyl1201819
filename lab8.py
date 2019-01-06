
from turtle import *
import random
import turtle
import math
class Ball(Turtle):
	def __init__(self,x,y,dx,dy,radius,color):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius = radius
		self.color(color)
		self.goto(x,y)
		self.dx = dx
		self.dy = dy
		#self.width = width
		#self.height = height
	
	def move(self, height, width):
		oldx = self.xcor()
		oldy = self.ycor()
		newx = oldx + self.dx
		newy = oldy + self.dy
		
		left_side = newx - self.radius
		right_side = newx + self.radius
		top_side = newy + self.radius
		bottom_side = newy - self.radius
		self.height = height
		self.width = width
		if top_side > self.height:
			self.dy = -self.dy
		elif bottom_side < -height:
			self.dy = -self.dy
		elif right_side > width :
		 	self.dx = -self.dx

		elif left_side < -width:
			self.dx = -self.dx
		self.goto(newx,newy)
		
def check_collision(ball_1,ball_2):
	x1 = ball_1.xcor()
	y1 = ball_1.ycor()
	x2 = ball_2.xcor()
	y2 = ball_2.ycor()
	D = math.sqrt(math.pow((x2-x1),2) + math.pow((y2-y1),2))
	sum_radius = ball_1.radius + ball_2.radius
	if sum_radius > D:
		ball_1.color("green")
		ball_2.color("pink")
		print("change radius")
		
	else:
		print("you are done")
ball_1 = Ball(100,100,5,4,20,"pink")
ball_2 = Ball(50,50,4,3,25,"blue")

while 1==1:
	ball_1.move(300,300)
	ball_2.move(300,300)
	check_collision(ball_1,ball_2)
turtle.mainloop()
