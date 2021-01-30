# list is a sequence
strings = ['hello', 'world']
numbers = [17, 123]
empty = []


# lists are mutable
numbers = [17, 123]
numbers[1] = 5
print(numbers)

# traversing a list

for i in numbers:
	print(i)

for i in range(len(numbers)):
	print(numbers[i])

