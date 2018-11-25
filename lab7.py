from turtle import *
import random
import turtle
import math
class Ball(Turtle):
	def __init__(self,radius,color,speed):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius = radius
		self.color(color)
		self.speed(speed)
def check_collision(ball_1,ball_2):
	x1 = ball_1.xcor()
	y1 = ball_1.ycor()
	x2 = ball_2.xcor()
	y2 = ball_2.ycor()
	D = math.sqrt(math.pow((x2-x1),2) + math.pow((y2-y1),2))
	sum_radius = ball_1.radius + ball_2.radius
	if sum_radius > D:
		#ball_1.color("green")
		#all_2.color("pink")
		print("change radius")
	else:
		print("you are done")

ball_1 = Ball(20,"red",2)
ball_1.pu()
ball_1.goto(90,30)
ball_2 = Ball(25,"blue",2)
check_collision(ball_1,ball_2)
print(ball_1.pos())
turtle.mainloop()