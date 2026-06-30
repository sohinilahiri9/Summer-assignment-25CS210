# Marksheet Generation System
name = input("Enter student name: ")
roll = int(input("Enter roll no: "))

m1 = int(input("Enter marks in Subject 1: "))
m2 = int(input("Enter marks in Subject 2: "))
m3 = int(input("Enter marks in Subject 3: "))
m4 = int(input("Enter marks in Subject 4: "))
m5 = int(input("Enter marks in Subject 5: "))

total = m1 + m2 + m3 + m4 + m5
per = total / 5

if per >= 90:
    grade = 'A+'
elif per >= 80:
    grade = 'A'
elif per >= 70:
    grade = 'B'
elif per >= 60:
    grade = 'C'
elif per >= 50:
    grade = 'D'
else:
    grade = 'F'

print("\n--------- MARKSHEET ---------")
print("Name:", name)
print("Roll No:", roll)
print("Subject 1:", m1)
print("Subject 2:", m2)
print("Subject 3:", m3)
print("Subject 4:", m4)
print("Subject 5:", m5)
print("Total Marks:", total, "/ 500")
print("Percentage:", per, "%")
print("Grade:", grade)
print("-----------------------------")

if grade == 'F':
    print("Result: FAIL")
else:
    print("Result: PASS")