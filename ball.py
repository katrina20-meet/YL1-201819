from turtle import*
class Ball(Turtle):
	def __init__ (self,x,y,dx,dy,r,color):
		 Turtle.__init__(self)
		 self.penup()
		 self.x= x
		 self.y= y
		 self.dx= dx
		 self.dy= dy
		 self.r= r
		 self.shape("circle")
		 self.shapesize(r/10)
		 self.color(color)
		 self.goto(x,y)

	def move(self,screen_width, screen_height):
		curent_x = self.xcor()
		new_x= self.dx + self.xcor()
		current_y= self.ycor()
		new_y = self.dy + self.ycor()
		right_side_ball = new_x + self.r
		left_side_ball = new_x - self.r
		top_side_ball = new_y + self.r
		bottom_side_ball = new_y - self.r
		self.goto(new_x, new_y)

		#check collisions with borders
		self.screen_width= screen_width
		self.screen_height = screen_height
		if(right_side_ball>= (self.screen_width)):
			self.dx= -self.dx
		if(left_side_ball<= -(self.screen_width)):
			self.dx= -self.dx
		if(top_side_ball>= (self.screen_height)):
			self.dy= -self.dy
		if(bottom_side_ball<= -(self.screen_height)):
			self.dy= -self.dy

	def new_ball(self,x,y,dx,dy,r,color):
		self.penup()
		self.x= x
		self.y= y
		self.dx= dx
		self.dy= dy
		self.r= r
		self.shape("circle")
		self.shapesize(r/10)
		self.color(color)
		self.goto(x,y)



