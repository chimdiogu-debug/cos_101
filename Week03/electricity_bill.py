
customer_name = input ("Enter customer's name: ")
energy_consumed = float(input("Enter energy consumed in kwh: "))

if energy_consumed < 0:
    print ("Invalid consumption. Energy can not be negative.")
else:
    if energy_consumed <= 50:
        bill = energy_consumed * 50
    elif energy_consumed <= 150:
        bill = (50 * 50) + ((energy_consumed - 50) * 75)
    else:
        bill = (50 * 50) + (100 * 75) + ((energy_consumed - 100) * 150)
print ()
print ("ELECTRICITY BILL")
print (f"Customer: {customer_name}")
print (f"Energy Consumed: {energy_consumed:.2f}kwh")
print (f"Total bill: NGN{bill:,.2f}")











