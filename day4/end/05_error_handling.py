# def one(a):
# 	if type(a) == int:
# 		print(a + 5)
# 	print("error")

# one("hello")





# 01
# 1 / 0


# # 02
# try:
# 	5 + "6"
# except Exception as e:
# 	print(e)




# # 03

# try:
# 	1 / 0
# except:
# 	print("You cannot divide by zero!")



# # 04

# def odd(n):
# 	if n % 2 == 0:
# 		raise Exception
# 	else:
# 		print("ok")
# try:
# 	odd(2)
# except Exception as e:
# 	print("not odd")





# # 05
# def divide(a,b):
# 	try:
# 		result = a/b
# 	except (ZeroDivisionError, TypeError) as err:
# 		print("Something went wrong!")
# 		print(err)
# 	else:
# 		print(f"{a} divided by {b} is {result}")

# print(divide(1,2))
# print(divide(1,'a'))
# print(divide(1,0))