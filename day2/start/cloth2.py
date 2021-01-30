r_width = 140
price_per_metre = 5

w_height = input('Enter the height of the w (cm): ')
	w_width = input('Enter the width of the w (cm): ')

c_width = (w_width * 0.75) + 20

if c_length < r_width:
	total_length = (c_width * 2) / 100
elif c_width > r_width:
	if extra_material < (r_width / 2):
	widths +=1
else:
	total_length = (c_length * 2) / 100

print('total:', round(total_length, 2))

price = total_length * price_per_metre
print('price:', round(price, 2))

