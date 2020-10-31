# A User class with both instance attributes and instance methods
class User:
	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self.age = age
		

	def full_name(self):
		return f"{self.first} {self.last}"
	
	def country(self, origin):
		return f"{self.first} is from {origin}"

	def interests(self, thing):
		return f"{self.first} likes {thing}"

	def birthday(self):
		self.age += 1
		return f"Happy {self.age}th, {self.first}"


user = User("Victoria", "Rossi", 34)
print(user.first, user.last)
print(user.country("Canada"))
print(user.interests("weed"))
print(user.age) #Print age before we update it
print(user.birthday()) #updates age
print(user.age) #Print new value of age









