weight = int(input())
ticketprice = int(input())
if weight == 0:
    total = ticketprice - 10
else:
    if weight > 15:
        bagcharge = (weight - 15) * 4
        total = ticketprice + bagcharge
    else:
        total = ticketprice
print(total)
