#programmer's name : Suhadah
#problem description:  calculates the amount of the bill to be paid after receiving the discount.

usage = float(input("Enter your monthly usage : ")) #ask user for input

#determine discount percentage
if usage < 50:
    discount = 0

elif usage <= 100:
    discount = 0.05

else:
    discount = 0.20

#calculate bill based on discount and usage
discount_amount = usage * discount
bill = usage - discount_amount

#display amount of the bill to be paid
print(f"Amount to be paid : RM{bill:.2f}")