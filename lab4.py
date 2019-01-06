
class Animal(object):
	def __init__(self,sound,name,age,favorite_color):
		self.sound = sound
		self.name = name
		self.age = age
		self.favorite_color = favorite_color
	def eat(self,food):
		print("yummy!!"+ self.name + "is eating "+ "" + food)
	def description(self):
		print(self.name + " is " +str(self.age )+ "years old and loves the color" + self.favorite_color)
	def make_sound(self):
		print(self.sound*3)
i = Animal("meaw", "cat",2,"blue")
i.eat("fish")
i.description()
i.make_sound()

class Person(object):
	def __init__(self,name,age,city,gender):
		self.name = name
		self.age = age
		self.city = city
		self.gender = gender
	def eat_breakfast(self,favorite_breakfast):
		print(self.name +" " + "is" + " "+ "eating" + " "+ favorite_breakfast)
	def study(self,subject):
		print(self.name + " "+ "is"+ " "+ "studying"+" " + subject)

p = Person("Joyce",14,"bethlehem","female")
p.eat_breakfast("eggs")
p.study("English")

'''
