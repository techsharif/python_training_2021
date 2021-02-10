from rdata import Row, Data


# calculate data from files

file = open("apache.log", "r")

data = file.read()
first_line = data.split("\n")[0]
print(first_line)
first_line  = first_line.replace("-",'')
first_line  = first_line.replace("[",'')
first_line  = first_line.replace("]",'')
line_data = first_line.split(" ")
line_data.pop(5)
line_data.pop(2)
print(line_data)
file.close()

row = Row(*line_data)
print(row.phone)
