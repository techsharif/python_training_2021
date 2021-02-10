# # 01
# 1 / 0


# # 02
# try:
# 	1 / 0
# except ZeroDivisionError:
# 	print("You cannot divide by zero!")





# # 03

# try:
# 	1 / 0
# except:
# 	print("You cannot divide by zero!")



# # 04

# n = 2
# if n % 2 == 0:
# 	raise Exception
# else:
# 	print("ok")




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