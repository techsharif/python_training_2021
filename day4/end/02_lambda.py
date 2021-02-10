# 01 
# map
# l = [1, 2, 3, 4]
# s = map(str, l)
# print(s)
# s1 = list(s)
# print(s1)

# # 02
# l = [1, 2, 3, 4]
# print(list(map(str, l)))


# # 03
# l = [1, 2, 3, 4]
# doubles = list(map(lambda x: x * 2, l))


# # 04
# names = [
#     {'first':'Rusty', 'last': 'Steele'}, 
#     {'first':'Colt', 'last': 'Steele', }, 
#     {'first':'Blue', 'last': 'Steele', }
# ]

# first_names = map( lambda name:  name["first"], names)
# first_names = list(first_names)

# # first_names = []
# # for name in names:
# # 	first_names += [name["first"]]


# print(first_names) # ['Rusty', 'Colt', 'Blue']




# # 05
# # def isEven(x):
# # 	return x % 2 == 0;

# # l = [1,2,3,4]
# # evens = list(filter(isEven, l))
# # print(evens)

# l = [1,2,3,4]
# evens = list(filter(lambda x: x % 2 == 0, l))
# print(evens)





# # 06
# users = [
# 	{"username": "samuel", "tweets": ["I love cake", "I love pie", "hello world!"]},
# 	{"username": "katie", "tweets": ["I love my cat"]},
# 	{"username": "jeff", "tweets": []},
# 	{"username": "bob123", "tweets": []},
# 	{"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
# 	{"username": "guitar_gal", "tweets": []}
# ]

# # To sort users by their username
# # users = sorted(users,key=lambda user: user["username"] )
# # print(users)

# # Finding our most active users...
# # Sort users by number of tweets, descending
# users = sorted(users,key=lambda user: len(user["tweets"]) , reverse=True)
# print(users)








# # 07
# songs = [
# 	{"title": "happy birthday", "playcount": 1},
# 	{"title": "Survive", "playcount": 6},
# 	{"title": "YMCA", "playcount": 99},
# 	{"title": "Toxic", "playcount": 31}
# ]

# # To sort songs by playcount
# sorted(songs, key=lambda s: s['playcount'])
