hour = int(input())
if hour < 2:
    fee = 0
else:
    if hour <= 5:
        fee = (2 * 0) + ((hour - 2) * 2)
    else:
        fee = (2 * 0) + (3 * 2) + ((hour - 5) * 3)
        if fee > 30:
            fee = 30
print(fee)
