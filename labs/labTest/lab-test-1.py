weight = int(input())
if weight >= 5:
    charge = (5 * 8) + ((weight - 5) * 6)
    if charge > 60:
        totalCharge = charge + 10
    else:
        totalCharge = charge
else:
    totalCharge = weight * 8
print(weight)
print(totalCharge)
