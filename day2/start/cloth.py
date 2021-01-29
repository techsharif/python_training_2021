r_width = 140
price_per_metre = 5

w_height = input('Enter the height of the w (cm): ')
w_width = input('Enter the width of the w (cm): ')

c_width = float(w_width) * 0.75 + 20
c_length = float(w_height) + 15

widths = c_width / r_width
total_length = c_length * widths

total_length = (total_length * 2) / 10

price = total_length * price_per_metre

print(f"You need {total_length:.2f} meters of cloth for {price:.2f}")