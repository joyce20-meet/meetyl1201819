'''
import turtle
angle=145
length=120
for i in range(5):
	turtle.forward(length)
	turtle.right(angle)
	
turtle.mainloop()

import turtle
for i in range(4):
	turtle.forward(50)
	turtle.left(90)
turtle.right(45)
turtle.forward(50)
turtle.left(115)
turtle.forward(50)



turtle.mainloop()
'''
import turtle
for i in range(500):
	#turtle.pd()
	turtle.forward(100)
	turtle.right(45)
	turtle.forward(50)
	turtle.right(100)
	turtle.forward(25)

	turtle.pu()
	turtle.home()
	turtle.right(i)
	turtle.pd()
	#turtle.home()
turtle.mainloop()