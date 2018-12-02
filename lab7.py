
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
		

	
	def move(self,width,height):
		self.width = width
		self.height = height
		oldx = self.xcor()
		oldy = self.ycor()
		newx = oldx + self.dx

		newy = oldy + self.dy
		self.goto(newx,newy)
		if newx > width:
			newx = -newx
		if newy > height:
		 	newy = -newy	
	



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
		#ball_1.forward(20)
	else:
		print("you are done")
ball_1 = Ball(100,100,5,4,20,"red")
ball_2 = Ball(50,50,4,3,25,"blue")

while True:
	ball_1.move(10,10)
	ball_2.move(10,10)
	check_collision(ball_1,ball_2)

turtle.mainloop()