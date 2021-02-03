# def function_name(parameters):
# 	statement(s)


# 01
def f1():
	print("Hello")
f1()



# 02
def f2(s):
	print(s)

f2("one")




# 03
def f3(s="Hello"):
	print(s)

f3()
f3("one")



# 04
def f4():
	return "hello"
f4()
print(f4())



# 05
def f5(x):
	if x < 0:
		return "Hello!"
	else:
		return 0

f5(1)
print(f5(-1))
print(f5(2))