r_width = 140
price_per_metre = 5

w_height = input('Enter the height of the w (cm): ')
w_width = input('Enter the width of the w (cm): ')

print()

c_width = (float(w_width) * 0.75) + 20
print('width:', round(c_width, 2))
c_length = float(w_height) + 15
print('height:', round(c_length, 2))


print('shorter?:', c_length < r_width)
print('wider?:', c_width > r_width)

if c_length < r_width:
	total_length = (c_width * 2) / 100
elif c_width > r_width:
	widths = int(c_width/r_width)
	extra_material = c_width%r_width
	if extra_material < (r_width / 2):
		widths +=1
	if extra_material > (r_width / 2):
		widths +=2
	print('widths:', widths)
	total_length = (c_length * widths) / 100
else:
	total_length = (c_length * 2) / 100

print('total:', round(total_length, 2))

price = total_length * price_per_metre
print('price:', round(price, 2))

print()
print("You need", round(total_length, 2), "meters of cloth, costing: ",round(price, 2))