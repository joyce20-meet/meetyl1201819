'''
import tkinter as tk
from tkinter import simpledialog
#Then when ever you want to ask the user for input use this code
greeting = simpledialog.askstring("Input", "Hello, possible pirate! What's the password?", parent=tk.Tk())
if i in greeting:
    print("Go away, pirate.")
else:
	print("Greetings, hater of pirates!")
'''
'''
import tkinter as tk
from tkinter import simpledialog

year = simpledialog.askstring("Input", "Greetings! What is your year of origin?", parent=tk.Tk().withdraw())

if year <= 1900:
    print ("Woah, that's the past!")
elif year > 1900 and year < 2020:
    print ("That's totally the present!")
else:
    print ("Far out, that's the future!!")
'''
'''
class Person(object):
	def __init__(self,first_name ,last_name):
		self.first_name = first_name
		self.last_name = last_name
	def speak(self):
		print("My name is" + self.first_name + " " + self.last_name)
Me = Person("Brandon","walsh")
You = Person("Ethan","Reed")
Me.speak()
You.speak()

import tkinter as tk
from tkinter import simpledialog
exam_one = int(simpledialog.askstring("Input", "Input exam grade one: ", parent=tk.Tk().withdraw()))

exam_two = int(simpledialog.askstring("Input ","exam grade two: ", parent=tk.Tk().withdraw()))

exam_three =  int(simpledialog.askstring("Input"," exam grade three: ", parent=tk.Tk().withdraw()))

grades = [exam_one, exam_two ,exam_three]
sum = 0
for grade in grades:
  sum_1 = sum + grade

avg = sum / len (grades)

if avg >= 90:
    letter_grade = "A" 
elif avg >= 80 and avg < 90:
    letter_grade = "B"
elif avg > 69 and avg < 80:
    letter_grade = "C"
elif avg <= 69 and avg >= 65:
    letter_grade = "D"
else:
    letter_grade = "F"

for grade in grades:
    print("Exam: " + str(grade))

    print("Average: " + str(avg))

    print("Grade: " + str(letter_grade))

if letter_grade is "F":
    print ("Student is failing.")
else:
    print ("Student is passing.")


class Person(object):
   def __init__(self, name, favorite_food ,age , color):
       self.name = name
       self.favorite_food = favorite_food
       self.age = age
       self.color = color

   def define_color(self):
        print("my favourite color is" + " "+ self.color)

   def print_info(self):
       print("My name is " + self.name + " I'm " + str(self.age) + " years old.")
       print("My favorite food is " + self.favorite_food + " and my favorite color is " + " " + self.color)


a = Person("Britney", "Pizza", "16", "black")
a.define_color()
a.print_info()

b = Person("Jake", "burger" , "15","green")
b.print_info()

class Bear(object):
    def __init__(self, name):
    	self.name = name 
    
    def say_hi(self):
        print("Hi! I’m a bear. My name is " + self.name)
my_bear = Bear('Danny')
my_bear.say_hi()

balloons = 5
name = "Ron"
color = "Yellow"
print("This is a tale about " + str(balloons )+ " balloons. The first kid is " + name + " who got a " + color +" "+ "balloon")

class Cake(object):
    def __init__(self,cake_flavor):
        self.cake_flavor = cake_flavor

    def eat(self):
        print("Yummy!!! Eating a " +  self.cake_flavor +" " + "cake :)")

cake_1 = Cake("chocolate")
cake_1.eat()
# what I want to be printed: Yummy!!! Eating a chocolate cake :)




class Cat(object):
	def __init__(self, name):
		self.name = name
	def birthday(self):
 		age=0
 		for age in range (8):	
 			age += 1
 			if age >= 100:
 				print("Dong dong, the cat is dead!")
 			else:
					print(self.name + " hasing it's "+ str(age) + " birthday ! ")

my_cat = Cat("Salem")
my_cat.birthday()
'''
