class person():
	def __init__ (self,name,age,city, gender, job):
		self.name= name
		self.age= age
		self.city= city
		self.gender= gender
		self.job= job
	def eat(self, food):
		self.favfood=food 


per2= person("lala",4, "unicorn land", "female", "president")
per2.eat("toast")
print(per2)

