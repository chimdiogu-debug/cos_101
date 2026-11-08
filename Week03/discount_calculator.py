amount = float(input("Enter amount: "))

if amount < 0:
    print ("Invalid amount.")
else:
    if amount >= 50000:
        discount = 10
        print ("Discount is 10%")
    elif 10000 <= amount < 50000:
        discount = 5
        print ("Discount is 5%")
    else :
        discount = 0 
        print ("Discount is 0%")
    discount_amount = (discount/100) * amount
    final_amount = (amount - discount_amount)

    print()
    print(f"Original Amount: NGN{amount:,.2f}")
    print(f"Discount Amount: NGN{discount_amount:,.2f}")
    print(f"Final amount payable: NGN{final_amount:,.2f}")
