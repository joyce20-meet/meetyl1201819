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
'''
import tkinter as tk
from tkinter import simpledialog
exam_one = int(simpledialog.askstring("Input", "Input exam grade one: ", parent=tk.Tk().withdraw()))

exam_two = int(simpledialog.askstring("Input ","exam grade two: ", parent=tk.Tk().withdraw()))

exam_three = str(simpledialog.askstring("Input"," exam grade three: ", parent=tk.Tk().withdraw()))

grades = [exam_one, exam_two ,exam_three]
sum = 0
for grade in grades:
  sum = sum + grade

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

if letter-grade is "F":
    print ("Student is failing.")
else:
    print ("Student is passing.")

