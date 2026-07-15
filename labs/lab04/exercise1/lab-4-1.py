kWh = int(input())
if kWh <= 100:
    bill = 0.3 * kWh
else:
    if kWh > 100 and kWh <= 200:
        bill = 100 * 0.3 + kWh - 100 * 0.5
    else:
        bill = 100 * 0.3 + 100 * 0.5 + kWh - 200 * 0.75
print(bill)
