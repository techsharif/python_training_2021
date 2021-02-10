import re

pattern = "^(((\+?880)|0)?1[6|8]\d{8})"


inp = open("sampleFile.txt", "r")
output = open("output.txt", "w")

for line in inp:
	phones = re.findall(pattern, line);
	# for phone in phones:
	# 	new_phone = phone[:-2] + "88"
	# 	line = line.replace(phone, new_phone)
	# output.write(line)
	print(phones)
