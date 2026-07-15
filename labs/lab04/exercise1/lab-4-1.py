kWh = int(input())
if kWh <= 100:
    charges = 0.3
else:
    if kWh > 100 and kWh <= 200:
        charges = 0.5
    else:
        charges = 0.75
bill = charges * kWh
print(bill)
