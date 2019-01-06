from turtle import *
import random
import turtle
import math

class Ball(Turtle):
	def __init__(self,x,y,dx,dy,radius,color):
		Turtle.__init__(self)
		self.shape("circle")
		self.radius = radius
		self.shapesize(radius/10)
		self.color(color)
		self.pu()
		self.goto(x,y) 
		self.dx = dx
		self.dy = dy
		self.radius = radius

	def move(self,height,width):
		oldx = self.xcor()
		oldy = self.ycor()
		newx = oldx + self.dx
		newy = oldy +self.dy
		right_side_ball = newx + self.radius
		left_side_ball = newx - self.radius 
		up_side_ball = newy + self.radius
		down_side_ball = newy - self.radius
		
		self.height = height
		self.width = width
		if up_side_ball > self.height:
			self.dy = -self.dy
		elif down_side_ball < -self.height:
			self.dy = -self.dy
		elif right_side_ball > self.width :
		 	self.dx = -self.dx

		elif left_side_ball < -self.width:
			self.dx = -self.dx
		self.goto(newx,newy)

#turtle.mainloop()