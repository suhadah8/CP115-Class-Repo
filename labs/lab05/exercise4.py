item_name = input("item name : ")
item_price = float(input("item price : "))

quantity = 3
tax_rate = 0.06

subtotal = item_price * quantity
total_cost = subtotal + tax_rate

print(subtotal)
print("tax amount : " , tax_rate)
print(total_cost)