print("============ QUESTION 1 ===========")
#QUESTION 1
num1 = int (input("Enter First Number: "))
num2 = int (input("Enter Second number: "))
num3 = int (input("Enter Third number: "))
avg = (num1+num2+num3)/3
print("The average is :",avg)
print("============ QUESTION 2 ===========")
#QUESTION 2
income = int(input("Please enter your income: "))
dependents = int(input("Please enter number of dependents: "))
sd = 10000

taxable = income - sd - (dependents*3000)
tax = taxable*0.2
print("Total Payable tax is: ",tax)
print("============ QUESTION 3 ===========")

#QUESTION 3
student =[]
SID = int(input("Enter your SID: "))
Name = str(input("Enter your name: "))
Gender = str(input("Enter your Gender(M/F/U): "))
C_name = str(input("Enter your Course: "))
cg = float(input("Enter your cgpa: "))

student.append(SID)
student.append(Name)
student.append(Gender)
student.append(C_name)
student.append(cg)

print(student)
print("============ QUESTION 4 ===========")
#QUESTION 4
list = []
s1 = int(input("Marks of 1st student : "))

s2 = int(input("Marks of 2nd student : "))

s3 = int(input("Marks of 3rd student : "))

s4 = int(input("Marks of 4th student : "))

s5 = int(input("Marks of 5th student : "))

list.append(s1)
list.append(s2)
list.append(s3)
list.append(s4)
list.append(s5)

print("The list of marks of students is : ",list)

print("============ QUESTION 5 ===========")
#QUESTION 5
color = [ 'Red','Green','White','black','Pink','Yellow']
color.remove('black')
print("Updated list: ",color)
color[3] = ('purple')
print(color)
