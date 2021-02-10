# # 01
# def print_square_of_7():
# 	print(7**2)

# print_square_of_7()

# def square_of_7(): 
# 	print("I AM BEFORE THE RETURN!")
# 	return 7**2
# 	print("I AM AFTER THE RETURN!")

# result = square_of_7()
# print(result)




# 02
# remove unnecessary codes
# def is_odd_number(num):
#     return num % 2 != 0

# print(is_odd_number(4))


# # 03
# def feed_me(*stuff):
# 	print(*stuff)
# 	print(type(stuff))

# feed_me(1, 2, 3)
# feed_me(1, 2, 3, 4, 5)





# # 04
# def feed_me(*stuff):
# 	for thing in stuff:
# 		print(f"YUMMY I EAT {thing}")
# feed_me("apple", "tire", "shoe", "salmon")





# # 05
# def sum_all_nums(*nums):
# 	total = 0
# 	for num in nums:
# 		total += num
# 	return total
	
# print(sum_all_nums(4,6,9,4,10))
# print(sum_all_nums(4,6))




# 06
# def fav_colors(**kwargs):
# 	# print(kwargs)
# 	print(kwargs["a"])

# fav_colors(a = 1, b = 2)


# def one(a, b, c, d=6, e=7):
# 	print(a, b, c, d, e)


# one(c = 1, b = 2, a = 3)
# one(3, 2, 1)

# # 07
# def fav_colors(**kwargs):
# 	for person, color in kwargs.items():
# 		print(f"{person}'s favorite color is {color}")

# 	# for person in kwargs:
# 	# 	print(f"{person}'s favorite color is {kwargs[person]}")

# fav_colors(one="purple", two="red", three="green")
# fav_colors(one="purple", two="red", three="green", four = "blue")
# fav_colors(one="purple")



# # 08
# def display_info(a, b, *args, instructor="one", **kwargs):
#   return [a, b, args, instructor, kwargs]

# print(display_info(1, 2, 3, instructor="two", last_name="Steele", job="Instructor"))
# print(display_info(1, 2, "three", last_name="Steele", job="Instructor"))
# print(display_info(1, 2, 3, "three", last_name="Steele", job="Instructor"))
# print(display_info(1, 2, 3, 4, 5, last_name="Steele", job="Instructor"))


# # 05

# data = [4,6,9,4,10]
# def sum_all_nums1(*nums):
# 	print(type(nums))
# 	# nums[1] = 3;
# 	total = 0
# 	for num in nums:
# 		total += num
# 	return total
	
# print(sum_all_nums1(*data))


# def sum_all_nums2(nums):
# 	print(type(nums))
# 	nums[1] = 3;
# 	total = 0
# 	for num in nums:
# 		total += num
# 	return total
	
# print(sum_all_nums2(data))
# print(data)


# a, b = 1, 2
# print(a, b)
# a, b = [1, 2]
# print(a, b)

# data = {"one": 1, "two": 2}
# def one(**args):
# 	print(args)

# one(**data)


# a, *b, c = 1, 2, 3, 4, 5
# print(a, b, c)