f = open("test.txt", "w")
data = '''“One fish. Two fish. Red fish. Blue fish.”'''
count_word = 0 
f.write(data)
f.close()

 
file = open("test.txt", "r")
rd = file.read()
wc = rd.split()
print (rd, "has " ,len(wc), " words")