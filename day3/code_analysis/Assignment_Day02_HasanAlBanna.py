# Read file

input_file='C:/Users/hasan.banna/Downloads/Python-Day02/Assignment/SampleText.txt'

with open(input_file, 'r') as f:
	data = f.read()
	
# print((data)

# Count letters (alpha)
count=0
for c in data:
	if c.isalpha():
		count += 1

print("Letters(s) :", count)


# Count words (spaces+1)
count=0
for c in data:
	if c == ' ':
		count += 1

print("Words(s) :", count+1)


# Count sentences (.!?)
count=0
for c in data:
	if c == '.' or c == '!' or c == '?':
		count += 1
		
print("Sentence(s) :", count)