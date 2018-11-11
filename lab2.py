'''
a=[1,2,3,4,5]
def number_list ():
	print (a[0],a[4])
	
number_list()
number_list=[1,2,3,4,6,7]
def num_list2 (x):
	for number in number_list:
		if number <= 5:
			print (number)
num_list2(number_list)
a=[1,2,3,4]
b=[2,3,5,6]
list_1=[1,2,3,4,5,6,8]
list_2=[2,3,4,5,6,7]
list_3=[]
for x in list_1:
	for y in list_2:
		if x==y:
			list_3.append(x)
print (list_2) 

import tkinter as tk
from tkinter import simpledialog
answer = int(simpledialog.askstring("Input","what number do you want?", parent=tk.Tk().withdraw()))
if answer > 1:
	for i in range(2,answer):
	
		if (answer % i)==0:
			print(answer,"is not a prime ")
			break
	else:
		print(answer,"is a prime")
			
'''
		
	
		 