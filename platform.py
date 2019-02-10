import turtle
from turtle import*
import random
import math
import time



class Platform(Turtle):
	def __init__(self, x, y, dy, width,gap):
		Turtle.__init__(self)
		self.pu()
		turtle.ht()
		self.goto(x,y)
		self.dy=dy
		self.width=width
		self.gap=gap
		self.shape("square")
		#register shape of the platform and change it

	def move(self):
		old_x = self.xcor()
		old_y = self.ycor() 
		new_y = old_y-self.dy
		self.goto(old_x,new_y)
'''
print( turtle.getcanvas().winfo_width()//2)
print( turtle.getcanvas().winfo_height()//2)
p= Platform(0,-200,2,0,0)
while True:
	p.move()
turtle.mainloop()