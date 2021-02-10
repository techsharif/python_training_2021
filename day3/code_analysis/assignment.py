file=open("file.txt", "r");
data = file.read()
file.close()
letter=0
words=0
sentences=0
#print(dir(data))


#letters
for i in data:
  if (i.isalpha()):
    letter+=1

#words
words= len(data.split())

#sentences
sentences= data.count(".")+data.count("!")+data.count("?")


print(letter, "letter(s)")
print(words, "word(s)")
print(sentences, "sentence(s)")