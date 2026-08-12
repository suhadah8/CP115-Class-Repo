coffee_price = 3.50 #declare coffee price i love spanish latte
coffee_quantity = 2
coffee_total = coffee_price * coffee_quantity

muffin_price = 2.10 #yummy delicious muffin
muffin_quantity = 3
muffin_total = muffin_price * muffin_quantity

water_price = 1.05 # keep hydrated bestieeee
water_quantity = 4
water_total = water_price * water_quantity

subtotal = water_total + muffin_total + coffee_total
tax = subtotal * 0.06
total = subtotal + tax


print("========== RECEIPT ==========\n"
    "Item\t\tPrice\tQty\tTotal\n"
    f"Coffee\t\t${coffee_price}\t{coffee_quantity}\t{coffee_total}\n"
    f"Muffin\t\t${muffin_price}\t{muffin_quantity}\t{muffin_total:.2f}\n"
    f"Water\t\t${water_price}\t{water_quantity}\t{water_total}\n"
    "------------------------------\n"
    f"Subtotal\t  ${subtotal}\n" 
    f"Tax (6%)\t  #{tax}\n"
    f"Total\t  {total}\n"
    "============================"
)