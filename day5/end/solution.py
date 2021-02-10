from rdata import Row, Data


# calculate data from files

file = open("apache.log", "r")
rows = []
data = Data();
# 02/Feb/2021:18:33:40 147.173.81.53  01882107078 prepaid  packs 563 "GET HTTP/1.0" 200 912198
for line in file:
	line  = line.replace("-",'')
	line  = line.replace("[",'')
	line  = line.replace("]",'')
	line_data = line.split(" ")
	line_data.pop(5)
	line_data.pop(2)
	row = Row(*line_data)
	rows += [row]
	data.add(row)
	break
file.close()

print(data.__dict__)



