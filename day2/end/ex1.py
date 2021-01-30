file = open("in1.txt", 'r');
data = file.read()
file.close()
# print(data)

lines = data.split('\n')

# file = open("out1.txt", "w");
# for l in lines:
# 	d = l.split(",")
# 	# d.pop()
# 	print(d[0]+"-"+d[2])
# 	file.write(d[0]+"-"+d[2]+"\n")
# file.close()

# file = open("out1.txt", "w");
# for l in lines:
# 	d = l.split(",")
# 	d.pop(1)
# 	o = "-".join(d) # "-".join('a', 'b', 'c')
# 	print(o)
# 	file.write(o + "\n")
# file.close()


out = []

for l in lines:
	d = l.split(",")
	d.pop(1)
	o = "-".join(d) # "-".join('a', 'b', 'c')
	out.append(o)
	
file = open("out1.txt", "w");
file.write("\n".join(out))
file.close()