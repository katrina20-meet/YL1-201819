#problem1

#import tkinter as tk
#from tkinter import simpledialog

#greeting = simpledialog.askstring("Input", "Hello, possible pirate! What's the password?", parent=tk.Tk().withdraw())
#if greeting in ["Arrr!"]:
#	print("Go away, pirate.")
#else:
#	print("Greetings, hater of pirates!")

#problem2:

#import tkinter as tk
#from tkinter import simpledialog

#year =simpledialog.askinteger("Input", "Greetings! What is your year of origin?", parent=tk.Tk().withdraw())

#if year <= 1900:
 #   print ("Woah, that's the past!")
#elif year > 1900 and year < 2020:
 #   print ("That's totally the present!")
#else:
 #   print ("Far out, that's the future!!")

#problem3:
#class Person():
 # def __init__(self, first_name, last_name):
  #  self.first_name = first_name
   # self.last_name = last_name
  #def speak(self):
  #	print("My name is" + " " + self.first_name + " " + self.last_name)

#me = Person("Brandon", "Walsh")
#you = Person("Ethan", "Reed")

#me.speak()
#you.speak()

#problem4:
#import tkinter as tk
#from tkinter import simpledialog

#exam_one = simpledialog.askinteger("Input", "Input exam grade one: ", parent=tk.Tk().withdraw())

#exam_two = simpledialog.askinteger("Input", "exam grade two:" , parent=tk.Tk().withdraw())

#exam_three= simpledialog.askinteger("Input", "exam grade three: ", parent=tk.Tk().withdraw())

#grades = [exam_one, exam_two, exam_three]
#sum = 0
#for grade in grades:

 # sum = sum + grade

#avg = sum / len(grades)

#if avg >= 90:
 #   letter_grade = "A"
#elif avg >= 80 and avg < 90:
 #   letter_grade = "B"
#elif avg > 69 and avg < 80:
 #   letter_grade = "C"
#elif avg <= 69 and avg >= 65:
 #   letter_grade = "D"
#else:
 #   letter_grade = "F"

#for grade in grades:
 #   print("Exam: " + str(grade))

  #  print("Average: " + str(avg))

   # print("Grade: " + letter_grade)

#if letter_grade is "F":
 #   print ("Student is failing.")
#else:
 #   print ("Student is passing.")

#problem5:

#class Person():
 #  def __init__(self, name, fav_food, age):
  #    self.fav_food = fav_food
   #   self.age = age


   #def define_color(self, color):
    #   self.color = color

   #def print_info(self):
    #   print("My name is " + self.name + ", I'm " + str(self.age) + " years old.")
     #  print("My favorite food is " + self.fav_food + " and my favorite color is " + self.color)


#a = Person("Britney", "Pizza", 16)
#a.define_color("Black")
#a.print_info()

#b = Person("Jake", "everything", 15)
#b.define_color("white")
#b.print_info()

#problem6:

#class Bear():
#	def __init__(self, name):

#		self.name=name
#		print("A new bear created. Its name is :"+ self.name )
	
#	def say_hi (self, my_name):
#		self.my_name= my_name
#		print("Hi! I’m a bear. My name is:"+ " " + self.my_name)
#my_bear = Bear("Danny")
#my_bear.say_hi("banana")

#problem7:

#balloons = 5
#name = "Ron"
#color = "Yellow"
#print("This is a tale about " + str(balloons) + " balloons. The first kid is " + name + " who got a " + color + "balloon")

#problem8:

#class Cake():
#	def __init__(self, flavor):
#		self.flavor = flavor

#	def eat(self):
#		print("Yummy!!! Eating a", self.flavor, "cake")

#cake = Cake("chocolate")
#cake.eat()

#problem9:

#class Cat():
#	def __init__(self, name, age):
#		self.name = name
#		self.age = age
#	def birthday(self):
#		self.age += 1
#		if self.age >= 100:
#			print("Ding dong, the cat is dead!")
#		else:
#			print(self.name, "hasing its", self.age,"th", "birthday!")

#my_cat = Cat("Salem", 3)
#my_cat.birthday()








