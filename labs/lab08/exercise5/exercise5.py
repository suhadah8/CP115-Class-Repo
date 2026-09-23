main_course = input()
drink = input()
dessert = input()

if main_course == "Chicken":
    mc_price = 10

elif main_course == "Beef":
    mc_price = 12

else:
    mc_price = 11

if drink == "Soft Drink":
    d_price = 2

else: 
    d_price = 3

if dessert == "Ice Cream":
    dst_price = 4

else:
    dst_price=5

food_cost = mc_price + d_price + dst_price
final_bill= (food_cost * 0.10) + food_cost

print(f"{final_bill:.2f}")
