'''
import turtle
angle=145
length=120
for i in range(5):
	turtle.forward(length)
	turtle.right(angle)
	
turtle.mainloop()

import turtle
turtle.begin_fill()
for i in range(4):
	turtle.forward(50)
	turtle.left(90)
turtle.right(45)
turtle.forward(50)
turtle.left(115.5)
turtle.forward(50)
turtle.end_fill()


turtle.mainloop()
import turtle
turtle.speed(0)
for i in range(365):
	
	turtle.forward(100)
	turtle.right(45)
	turtle.forward(50)
	turtle.right(100)
	turtle.forward(25)

	turtle.pu()
	turtle.home()
	turtle.right(i)
	turtle.pd()
turtle.mainloop()

import turtle
turtle.begin_fill()
turtle.fillcolor('blue')
turtle.circle(100)
#turtle.end_fill()
turtle.pu()
turtle.goto(100,-100)
turtle.pd()
turtle.circle(100)
turtle.pu()
turtle.goto(220,0)
turtle.pd()
turtle.circle(100)
turtle.pu()
turtle.goto(-125,-110)
turtle.pendown()
turtle.circle(100)
turtle.pu()
turtle.goto(-220,0)
turtle.pd()
#turtle.begin_fill()
#turtle.end_fill()
turtle.mainloop()
'''