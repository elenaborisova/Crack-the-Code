square_meters = float(input('Enter the number of square meters used: '))
total_cost = square_meters * 7.61
discounted_price = (total_cost * 0.18)

total_discounted_cost = total_cost - discounted_price

print(f'The final price is: {total_discounted_cost} lv.')
print(f'The discount is: {discounted_price} lv.')
