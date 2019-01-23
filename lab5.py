#from turtle import *
#import random
#colormode(255)
#class Square(Turtle):
	#def __init__(self,size):
	#	Turtle.__init__(self)
	##	self.shape("square")
	#def chngclor(self):
	#	self.color=random.randint(0,255)


from turtle import*
import turtle
class Hexagon(Turtle):
	def __init__ (self,size):
		Turtle.__init__(self)
		turtle.begin_poly()
		self.fd(50)
		self.right(60)
		self.fd(50)
		self.right(60)
		self.fd(50)
		self.right(60)
		self.fd(50)
		self.right(60)
		self.fd(50)
		self.right(60)
		self.fd(50)
		self.right(60)
		turtle.end_poly()
		p= turle.get_poly()
		register_shape("hexa", p)
		self.shape("hexa")
		self.fd(100)
hex1= Hexagon(40)

