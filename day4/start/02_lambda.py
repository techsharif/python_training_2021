# # 01 
# # map
# l = [1, 2, 3, 4]
# s = map(str, l)
# print(s)
# s = list(s)
# print(l)

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

# # first_names = TODO

# print(first_names) # ['Rusty', 'Colt', 'Blue']




# # 05
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
# # sorted(users,key= TODO )

# # Finding our most active users...
# # Sort users by number of tweets, descending
# # sorted(users,key=TODO , reverse=True)








# # 07
# songs = [
# 	{"title": "happy birthday", "playcount": 1},
# 	{"title": "Survive", "playcount": 6},
# 	{"title": "YMCA", "playcount": 99},
# 	{"title": "Toxic", "playcount": 31}
# ]

# # To sort songs by playcount
# sorted(songs, key=lambda s: s['playcount'])
