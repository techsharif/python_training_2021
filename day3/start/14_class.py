# class

# 01
# basic
# class Person(object):
# 	species = "Homo Sapiens"

# one = Person()
# print(one.species)



# 02
# __init__
# class Person(object):
# 	species = "Homo Sapiens"

# 	def __init__(self): 
# 		self.name = "default"

# one = Person()
# print(one.species)
# print(one.name)





# 03
# __init__ with arg
# class Person(object):
# 	species = "Homo Sapiens"

# 	def __init__(self, name): 
# 		self.name = name

# one = Person("one")
# print(one.species)
# print(one.name)





# 04
# __init__ with arg default
# class Person(object):
# 	species = "Homo Sapiens"

# 	def __init__(self, name="default"): 
# 		self.name = name

# one = Person("one")
# print(one.species)
# print(one.name)

# two = Person()
# print(two.species)
# print(two.name)


# class Number
# value
# __init__ (defalt  0)

# class Person(object):
# 	species = "Homo Sapiens"

# 	def __init__(self, name): 
# 		self.name = name

# class Number(object):
# 	def __init__(self, a = 0):
# 		self.value = a


# n = Number()
# print(n.value) # 0

# n = Number(5)
# print(n.value) # 5

# 05
# __str__
# class Person(object):
# 	species = "Homo Sapiens"

# 	def __init__(self, name="default"): 
# 		self.name = name

# 	def __str__(self):
# 		return f"{self.name} - {self.species}"

# one = Person("one")
# print(one)






# 06 
# user defined method
# class Person(object):
# 	species = "Homo Sapiens"

# 	def __init__(self, name): 
# 		self.name = name

# 	def __str__(self): 
# 		return self.name

# 	def rename(self, renamed): 
# 		self.name = renamed


# one = Person("one")
# print(one)
# one.rename("renamed")
# print(one)




# 07
# closer look

# import random
# class RandomClass(object):
# 	random1 = random.randint(0,9)

# 	def __init__(self): 
# 		self.random2 = random.randint(0,9)

# randomObj1 = RandomClass()
# print(randomObj1.random1)
# print(randomObj1.random2)

# randomObj2 = RandomClass()
# print(randomObj2.random1)
# print(randomObj2.random2)
