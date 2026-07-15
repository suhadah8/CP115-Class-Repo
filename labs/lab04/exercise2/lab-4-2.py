annualincome = float(input())
if annualincome <= 50000:
    totaltax = annualincome * 0
else:
    if annualincome >= 100000:
        totaltax = (50000 * 0) + (50000 * 0.01) + ((annualincome - 100000) * 0.02)
    else:
        totaltax = (50000 * 0.0) + annualincome - 50000 * 0.01
print(totaltax)
