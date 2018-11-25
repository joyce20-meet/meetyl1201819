
'''
from turtle import Turtle
import turtle
import random
turtle.colormode(255)
class Square(Turtle):
	def __init__(self,size):
		Turtle.__init__(self)
		self.shapesize(size)
		self.shape("square")

	def random_color(self):
		r = random.randint(0,256)
		g = random.randint(0,256)
		b = random.randint(0,256)
		self.color(r,g,b)

square1 = Square(5)
square1.random_color()
turtle.mainloop()

from turtle import Turtle
import turtle
turtle.begin_poly()
turtle.pd()
turtle.goto(50,0)
turtle.goto(80,-50)
turtle.goto(50,-100)
turtle.goto(0,-100)
turtle.goto(-30,-50)
turtle.goto(0,0)
turtle.register_shape("potato",(turtle.get_poly()))
turtle.mainloop()
turtle.end_poly()
class Hexagon(Turtle):
	def __int__(self):
		Turtle.__init__(self)
		self.shapesize(size) 
		self.shape("potato")

'''

#create a new class (:
