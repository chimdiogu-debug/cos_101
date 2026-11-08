#Pseudocode:
#START
    #INPUT student_name
    #INPUT daily_transport
    #INPUT daily_feeding
    #INPUT days
    #INPUT  other_expenses
    #transport_total= daily_transport * days
    #feeding_total= daily_feeding * days
    #weekly_total= transport_total + feeding_total + other_expenses
    #DISPLAY "WEEKLY EXPENSE SUMMARY"
    #DISPLAY student_name
    #DISPLAY trnsport_total, feeding_total, other_expenses,weekly_total
#END


#INPUT
student_name=input("Student Name:  ")
daily_transport=float(input("Daily Transport Cost:  "))
daily_feeding= float(input("Daily Feeding cost:  "))
days= int(input("Number of days on campus:  "))
other_expenses= float(input("Other expenses for the week:  "))

#CALCULATION
transport_total= daily_transport * days
feeding_total= daily_feeding * days
weekly_total= transport_total + feeding_total + other_expenses

#DISPLAY
print()
print("WEEKlY EXPENSE SUMMARY")
print("Student: ", student_name)
print(f"Transport total: NGN{transport_total:,.2f}")
print(f"Feeding total: NGN{feeding_total:,.2f}")
print(f"Other expenses: NGN{other_expenses:,.2f}")
print(f"Weekly total: NGN{weekly_total:,.2f}")

#Reasons why each input uses a string, integer, or float
#Student name uses a string because it is a text
#Daily transport cost a float becuase it is money and it could be in decimal
#Daily feeding cost uses a float becuase it is money and it could be in decimal
#Number of days on campus uses an integer because days are whole numbers
#Other expenses for the week uses a float beacause it is money and it could be in decimal


      
