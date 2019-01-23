from turtle import*
import random
import turtle
import math

class Ball(Turtle):
	def __init__(self, radius, color, speed):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius = radius
		self.color(color)
		self.speed(speed)

ball1=Ball(50, "yellow", 10)
ball2=Ball(40, "black", 10)

def check_collision(ball1,ball2):
	import math
	a=(ball1.xcor(),ball1.ycor(),ball1.radius)
	b=(ball2.xcor(),ball2.ycor(),ball2.radius)
	d= math.sqrt(math.pow(ball2.xcor()-ball1.xcor(),2)+ math.pow(ball2.ycor()-ball1.ycor(),2))
	if (ball1.radius+ball2.radius>=d):
		print("collision")
		turtle.colormode(255)
	else:
		print ("no collision")


check_collision(ball1,ball2)



turtle.mainloop()