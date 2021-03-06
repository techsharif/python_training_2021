# 01
# Polymorphism

# class Shark:
#     def swim(self):
#         print("The shark is swimming.")

#     def swim_backwards(self):
#         print("The shark cannot swim backwards, but can sink backwards.")

#     def skeleton(self):
#         print("The shark's skeleton is made of cartilage.")


# class Clownfish:
#     def swim(self):
#         print("The clownfish is swimming.")

#     def swim_backwards(self):
#         print("The clownfish can swim backwards.")

#     def skeleton(self):
#         print("The clownfish's skeleton is made of bone.")


# # Test 01
# sammy = Shark()
# sammy.skeleton()

# casey = Clownfish()
# casey.skeleton()


# # Test 02
# for fish in (sammy, casey):
#     fish.swim()
#     fish.swim_backwards()
#     fish.skeleton()


# # Test 03
# def in_the_pacific(fish):
#     fish.swim()

# sammy = Shark()
# casey = Clownfish()

# in_the_pacific(sammy)
# in_the_pacific(casey)







# 02
# Overloading

# class Vehicle:
# 	def __init__(self,tires):
# 		"""Constructor"""
# 		self.tires = tires


# 	def __add__(self, other):
# 		temp = Vehicle(0)
# 		temp.tires =  self.tires + other.tires
# 		return temp


# # init an object
# v1 = Vehicle(5)
# v2 = Vehicle(6)
# v3 = v1 + v2


# print(v1.tires)
# print(v2.tires)
# print(v3.tires)






# 03
# Inheritance

# # base class
# class Vehicle:
# 	def __init__(self, color, doors, tires, vtype):
# 		self.color = color
# 		self.doors = doors
# 		self.tires = tires
# 		self.vtype = vtype

# 	def brake(self):
# 		"""
# 		Stop the car
# 		"""
# 		return f"{self.vtype} braking"

# 	def drive(self):
# 		"""
# 		Drive the car
# 		"""
# 		return f"I'm driving a {self.color} {self.vtype}!"


# # Sub Class / Derived Class
# class Car(Vehicle):
# 	def brake(self):
# 		return "The car class is breaking slowly!"


# car = Car("yellow", 2, 4, "car")
# print(car.brake())
# print(car.drive())


# print(issubclass(SubClass,BaseClass))