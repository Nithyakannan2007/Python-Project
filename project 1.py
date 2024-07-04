#Use conditional statement and get the marks
# print the result for the following marks
# 90 to 100=A grade
# 80 to 90=B grade
# 70 to 80= C grade
# 60 to 70= D grade
# below 60= E grade
'''Get the student name and marks, print the total of marks,average
and give grades according to marks'''\

studName=(input("enter their name: "))
sub1=int(input("English: "))
sub2=int(input("Maths: "))
sub3=int(input("Physics: "))
sub4=int(input("Chemistry: "))
sub5=int(input("Computer: "))
sub6=int(input("Home Science: "))
sum=sub1+sub2+sub3+sub4+sub4+sub6
avg=(sum)/6
print("total= ",sum)
print("average= ",avg)
if(avg>90 and avg<=100):
    print("Grade: A")
elif(avg>80 and avg<=90):
    print("Grade: B")
elif(avg>70 and avg<=80):
    print("Grade: C")
elif(avg>60 and avg<=70):
    print("Grade: D")
else:
    print("Grade: E")