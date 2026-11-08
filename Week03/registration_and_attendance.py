registration_status = input("Registration complete? Enter yes or no: ")
attendance = float(input("Enter attendance percentage: "))

if registration_status != "yes" or "no":
     print ("Invalid, enter yes or no")
if 0 > attendance > 100:
    print ("Invalid attendance.")

if registration_status == "yes" and attendance >= 75:
    print ("You are qualified to right the exam.")
else:
    print("You are not qualified for the exam.")
S
