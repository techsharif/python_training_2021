f = open("test.txt", "r")
data = f.read()
print(data)
f.close()

f = open("test.txt", "w")
f.write("ok12")
f.close()

with open("test.txt") as f:
	data = f.read()
	print(data)

