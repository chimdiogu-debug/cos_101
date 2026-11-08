student_name= input ("Student name: ")
score= float(input("Enter Score: "))
if score <0 or score >100:
    print ("Invalid Score")
else:
    if score >= 70 :
        grade = "A"
    elif score >= 60:
        grade = "B"
    elif score>= 50:
        grade = "C"
    elif score >= 45:
        grade = "D"
    elif score >= 40:
        grade = "E"
    else :
        grade = "F"
print()
print("Student Name: ", student_name)
print("Score: ", score)
print("Grade: ", grade)
