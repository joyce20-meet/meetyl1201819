class Animal(object):
	def __init__(self,sound,name,age,favorite_food,favorite_color):
		self.sound = sound
		self.name = name
		self.age = age
		self.favorite_food = favorite_food
		self.favorite_color = favorite_color
	def eat(self,food):
		print("yummy!!"+ self.name + "is eating" + self.favorite_food)
	def description(self):
		print(self.name + "is" + self.age +'years old and loves the color' + self.favorite_color)
i = Animal("meaw", "cat","2","fish","blue")
i.eat(self)
i.description(self)
