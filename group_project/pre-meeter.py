import turtle
from turtle import*
import random
import math
import time

turtle.tracer(0,0)
turtle.hideturtle()
RUNNING = True
SLEEP = 0.0077
turtle.pu()
screen_width = turtle.getcanvas().winfo_width()//2
screen_height = turtle.getcanvas().winfo_height()//2

minimum_dy = 0.01
maximum_dy = 0.9
gap = 114
number_of_platforms= 8


def randomize_platform():
	x=random.uniform(width/2-screen_width, screen_width-width/2)
	y=screen_height

