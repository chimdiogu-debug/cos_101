#Problem: I want to calculate the number of chairs in the classroom.

#ALGORITHM:
    #1.Start
    #2.Input the number of rows
    #3.Input the number of chairs per row
    #4.Calculate total= rows * chairs
    #5.Display the total number of chairs in the class
    #6.Stop

#Pseudocode
    #START
    #Input rows
    #Input chairs
    #total= rows * chairs
    #Display "Total number of chairs in the class is ", total
    #END


#This program calculates the total number of chairs in the classroom.
#INPUT
rows= int(input("Input the number of Rows: "))
chairs= int(input("Input the number of Chairs per row: ")) 

#PROCESS
total=rows*chairs

#OUTPUT
print()
print ("Total number of chairs in the class is ",total)

