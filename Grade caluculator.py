#program to in put percentage of the student and return the mark
while 1:
    marks = float(input("Enter the mark of the student : "))
    if marks >= 90:
        print("A GRADE")
    elif marks >=75 and marks <90 :
        print("B GRADE")
    elif marks >=60 and marks <75 : 
        print("C GRADE")
    elif marks < 60:
        print("D GRADE")