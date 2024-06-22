#my solution
price=float(input("Enter your price: "))
taxe=float(0)
if price<=10000:
    taxe=0
elif price<=20000:
    taxe=10000*0.1
else:
    taxe=10000*0.1+(price-20000)*0.2
print("your taxe is: ",int(taxe),"$")
print("the total price is: ",int(price+taxe),"$")
'''
#their solution
income = 45000
tax_payable = 0
print("Given income", income)

if income <= 10000:
    tax_payable = 0
elif income <= 20000:
    # no tax on first 10,000
    x = income - 10000
    # 10% tax
    tax_payable = x * 10 / 100
else:
    # first 10,000
    tax_payable = 0

    # next 10,000 10% tax
    tax_payable = 10000 * 10 / 100

    # remaining 20%tax
    tax_payable += (income - 20000) * 20 / 100

print("Total tax to pay is", tax_payable)'''
