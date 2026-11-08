number = input("Enter a number greater than 1 or 'e' to exit: ")

while number!="e" and number != "exit":
    number = int(number)
    if number >1:
        for num in range (1,13):
            print (f"{num} * {number} = {num*number}")
    else:
        print("Invalid number.")

    number = input("Enter a number greater than 1 or 'e' to exit: ")
