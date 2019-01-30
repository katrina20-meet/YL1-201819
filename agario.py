import turtle
import time
import random
import math
from ball import Ball 
turtle.colormode(1)

turtle.tracer(0)
turtle.hideturtle()
global running
running=True
screen_width= turtle.getcanvas().winfo_width()/2
screen_height= turtle.getcanvas().winfo_height()/2
#creating object
my_ball= Ball(0,0,5,3,50,"purple")

def restart(x,y):
	global running
	running = True
	while(running):
		screen_width= turtle.getcanvas().winfo_width()/2
		screen_height= turtle.getcanvas().winfo_height()/2
		ppow.clear()
		again.hideturtle()
		movearound()
		move_all_balls()
		check_all_balls_collision()

		time.sleep(.1)
		turtle.update()


ppow=turtle.Turtle()
ppow.pu()
ppow.hideturtle()
again=turtle.Turtle()
again.pu()
turtle.register_shape("replay-button.gif")
again.shape("replay-button.gif")
again.goto(0,-70)

again.onclick(restart)
again.hideturtle()

number_of_balls= 5
minimum_ball_radius =10
maximum_ball_radius = 100
minimum_ball_dx= -5
maximum_ball_dx= 5
minimum_ball_dy = -5
maximum_ball_dy = 5

BALLS= []

for i in range(number_of_balls):
	x=random.randint(-screen_width+maximum_ball_radius, screen_width- maximum_ball_radius)
	y=random.randint(-screen_height+maximum_ball_radius, screen_height- maximum_ball_radius)
	if x == 0 and y == 0:
		x=random.randint(-screen_width+maximum_ball_radius, screen_width- maximum_ball_radius)
		y=random.randint(-screen_height+maximum_ball_radius, screen_height- maximum_ball_radius)	
	dx=random.randint(minimum_ball_dx, maximum_ball_dx) 
	dy=random.randint(minimum_ball_dy, maximum_ball_dy)
	r= random.randint(minimum_ball_radius, maximum_ball_radius)
	color=(random.random(), random.random(), random.random())

	new_balls= Ball(x,y,dx,dy,r,color)
	BALLS.append(new_balls)

def move_all_balls():
	for b in BALLS:
		b.move(screen_width, screen_height)

def collide(ball_a, ball_b):
	a=(ball_a.xcor(), ball_a.xcor(),ball_a.r)
	b=(ball_b.xcor(), ball_b.xcor(),ball_b.r)
	if (ball_a==ball_b):
		return False
	d=math.sqrt(math.pow(ball_b.xcor()-ball_a.xcor(),2)+math.pow(ball_b.ycor()-ball_a.ycor(),2))
	if (ball_a.r+ ball_b.r>=d):
		return True
	else :
		return False

def check_all_balls_collision():
	global running
	all_balls=[]
	all_balls.append(my_ball)
	for ball in BALLS:
		all_balls.append(ball)
	for ball_a in all_balls:
		for ball_b in all_balls:
			if(collide(ball_a, ball_b)):
				r1=ball_a.r
				r2= ball_b.r
				x=random.randint(-screen_width+maximum_ball_radius, screen_width- maximum_ball_radius)
				y=random.randint(-screen_height+maximum_ball_radius, screen_height- maximum_ball_radius)
				dx=random.randint(minimum_ball_dx, maximum_ball_dx) 
				dy=random.randint(minimum_ball_dy, maximum_ball_dy)
				while ((dx==0) and (dy==0)):
					dx=random.randint(minimum_ball_dx, maximum_ball_dx) 
					dy=random.randint(minimum_ball_dy, maximum_ball_dy)
				r= random.randint(minimum_ball_radius, maximum_ball_radius)
				color=(random.random(), random.random(), random.random())
				if (r1>r2):
					ball_b.new_ball(x,y,dx,dy,r,color)
					ball_a.r= ball_a.r+1.5


					ball_a.shapesize(ball_a.r/10)
					if (my_ball==ball_b):
						#turtle.bye()
						again.showturtle()
						running= False
						ppow.write("muahahaha Game over :p", align="center", font=("Purisa", 50, "normal"))
						again.onclick(restart)
				elif (r2>r1):
					ball_a.new_ball(x,y,dx,dy,r,color)
					ball_b.r= ball_b.r+1.5
					ball_b.shapesize(ball_b.r/10)
					if (my_ball==ball_a):
						again.showturtle()
						running= False
						ppow.write("muahahaha Game over :p", align="center", font=("Purisa", 50, "normal"))
				if ((ball_a.r>= screen_width*2) or (ball_b.r>=screen_width)):
					again.showturtle()
					running= False
					ppow.write("congrats!", align="center", font=("Purisa", 50, "normal"))
					
					
def movearound():
	x= turtle.getcanvas().winfo_pointerx() - screen_width*2
	y= screen_height*1.5 - turtle.getcanvas().winfo_pointery()
	my_ball.goto(x,y)


running= True
while(running):
	screen_width= turtle.getcanvas().winfo_width()/2
	screen_height= turtle.getcanvas().winfo_height()/2

	movearound()
	move_all_balls()
	check_all_balls_collision()

	time.sleep(.1)
	turtle.update()
	#again.penup()


turtle.mainloop()















