# VALIDATING EMAILS
'''
emails: 
colt@gmail.com
carly.simon@yahoo.com
rosa-98@meals.org

Starts with 1 or more letter,number,+,_,-,. 
thenA single @ sign 
then 1 or more letter, number, or -  
then A single dot 
then ends with 1 or more letter, number,-, or .  
'''

# https://www.shortcutfoo.com/app/dojos/python-regex/cheatsheet



# 01
# import re
# print(dir(re))




# # 2
# import re

# pattern = 'Hello'
# print(re.search(pattern, "onehelloonehelloone", re.IGNORECASE))
# print(re.findall(pattern, "onehelloonehelloone", re.IGNORECASE))
# print(re.search(pattern, "world"))




# # 03
# import re
# pattern = 'From'
# file = open('regex_test.txt')
# for line in file:
# 	line = line.strip()
# 	if re.search(pattern, line, re.IGNORECASE):
# 		print(line)





# # 03
# import re
# # Search for lines that start with 'From'
# pattern = '^From'
# file = open('regex_test.txt')
# for line in file:
# 	line = line.strip()
# 	if re.search(pattern, line, re.IGNORECASE):
# 		print(line)




# # 04
# import re
# # Search for lines that start with 'F', followed by
# # 2 characters, followed by 'm:'
# pattern = '^F..m'
# file = open('regex_test.txt')
# for line in file:
# 	line = line.strip()
# 	if re.search(pattern, line, re.IGNORECASE):
# 		print(line)






# # 05
# import re
# # Search for lines that start with From and have an at sign
# pattern = '^From:.+@'
# file = open('regex_test.txt')
# for line in file:
# 	line = line.strip()
# 	if re.search(pattern, line, re.IGNORECASE):
# 		print(line)








# # 06
# import re
# pattern = '^From:.+@'
# file = open('regex_test.txt')
# for line in file:
# 	line = line.strip()
# 	data = re.findall(pattern, line, re.IGNORECASE)
# 	if data:
# 		print(data)



# # 07
# import re
# pattern = '^From:.+@.+'
# file = open('regex_test.txt')
# for line in file:
# 	line = line.strip()
# 	data = re.findall(pattern, line, re.IGNORECASE)
# 	if data:
# 		print(data)




# # 08
# import re
# pattern = '.+@.+'
# file = open('regex.txt')
# for line in file:
# 	line = line.strip()
# 	data = re.findall(pattern, line, re.IGNORECASE)
# 	if data:
# 		print(data)




# # 09
# import re
# pattern = '\S+@\S+'
# file = open('regex_test.txt')
# for line in file:
# 	line = line.strip()
# 	data = re.findall(pattern, line, re.IGNORECASE)
# 	if data:
# 		print(data)


# # 10
# # ignoring <200801032127.m03LRUqH005177@nakamura.uits.iupui.edu>
# import re
# pattern = '[a-z]+@[a-z]+'
# file = open('regex_test.txt')
# for line in file:
# 	line = line.strip()
# 	data = re.findall(pattern, line, re.IGNORECASE)
# 	if data:
# 		print(data)


# + > 0
# * >= 0

# log.txt
# log1.txt

# log[0-9]*.txt


# # p = "ba*b"
# # s = "bbbb"
# 11
# ignoring <200801032127.m03LRUqH005177@nakamura.uits.iupui.edu>
# import re
# pattern = "([0-9a-z]+(\.[0-9a-z]+)*@[0-9a-z]+(\.[0-9a-z]+)+)"
# file = open('regex.txt')
# for line in file:
# 	line = line.strip()
# 	data = re.findall(pattern, line, re.IGNORECASE)
# 	if data:
# 		print(data)


# ([a-z0-9]+\.)+

# abc.def.ghi.

# # 12
# import re
# pattern = '(^Details:.*rev=([0-9.]+))'
# file = open('regex_test.txt')
# for line in file:
# 	line = line.strip()
# 	data = re.findall(pattern, line, re.IGNORECASE)
# 	if data:
# 		print(data)


# # 12
# import re
# pattern = '^Details:.*rev=([0-9.]+)'
# file = open('regex_test.txt')
# for line in file:
# 	line = line.strip()
# 	data = re.findall(pattern, line, re.IGNORECASE)
# 	if data:
# 		print(data)


# # 13
# import re
# # pattern = '^Details:.*[0-9.]+$'
# pattern = '^Details:.*[3]+$'
# file = open('regex_test.txt')
# for line in file:
# 	line = line.strip()
# 	data = re.findall(pattern, line, re.IGNORECASE)
# 	if data:
# 		print(data)

# # 13
# # \s -> white space
# # \S -> non white space
# # \d -> digit [0-9]
# # \D -> non digit
# # \w -> word
# # \W -> non word

# import re
# pattern = "\D+"
# line = "hel_.lo123 123.hello"
# data = re.findall(pattern, line, re.IGNORECASE)
# if data:
# 	print(data)


# 14
# . * + ? - | ^ [] {m,n}

# import re
# pattern = "[a-z]+\d{3}[^a-e]+"
# line = "hello123world"
# data = re.findall(pattern, line, re.IGNORECASE)
# if data:
# 	print(data)

# ip address 
