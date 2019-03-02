import turtle
from turtle import*
import random
import math
import time



class Platform(Turtle):
	def __init__(self, x, y,dx,dy,width,shape,screen_width):
		Turtle.__init__(self)
		self.pu()
		self.screen_width = screen_width
		turtle.ht()
		x = random.randint(-self.screen_width,self.screen_width)
		self.goto(x,y)
		self.dx = dx
		self.dy=dy
		self.width=width

		turtle.register_shape("meetlogo.gif")
		self.shape("meetlogo.gif")



	def move(self):
		oldx = self.xcor()
		oldy = self.ycor()
		newy = oldy - 0.05
		self.goto(oldx,newy)
		
		if self.ycor()<-400:
			print(self.xcor())
			x = random.randint(-self.screen_width,self.screen_width)
			self.goto(x,400)
		


# print( turtle.getcanvas().winfo_width()//2)
# print( turtle.getcanvas().winfo_height()//2)
# p= Platform(0,-200,0)
# p.shapesize(117/10)


