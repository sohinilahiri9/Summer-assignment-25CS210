# Complete Mini Project: Student Marksheet + Attendance System

students = [] 

def add_student():
    roll = int(input("Enter roll no: "))
    name = input("Enter name: ")
    m1 = int(input("Enter marks sub1: "))
    m2 = int(input("Enter marks sub2: "))
    m3 = int(input("Enter marks sub3: "))
    att = int(input("Enter attendance %: "))
    students.append([roll, name, m1, m2, m3, att])
    print("Student added successfully")

def display_all():
    print("\nRoll\tName\t\tM1\tM2\tM3\tTotal\tPer\tGrade\tAtt")
    for s in students:
        total = s[2] + s[3] + s[4]
        per = total / 3
        if per >= 90:
            grade = 'A+'
        elif per >= 80:
            grade = 'A'
        elif per >= 70:
            grade = 'B'
        elif per >= 60:
            grade = 'C'
        else:
            grade = 'F'
        print(s[0], "\t", s[1], "\t", s[2], "\t", s[3], "\t", s[4], "\t", total, "\t", round(per,2), "\t", grade, "\t", s[5], "%")

def search_student():
    roll = int(input("Enter roll to search: "))
    for s in students:
        if s[0] == roll:
            total = s[2] + s[3] + s[4]
            per = total / 3
            print("\n--- Student Details ---")
            print("Name:", s[1])
            print("Marks:", s[2], s[3], s[4])
            print("Total:", total, "/ 300")
            print("Percentage:", round(per,2), "%")
            print("Attendance:", s[5], "%")
            if s[5] < 75:
                print("Warning: Low Attendance")
            return
    print("Student not found")

def class_toppers():
    if len(students) == 0:
        print("No data")
        return
    top_per = 0
    top_name = ""
    for s in students:
        per = (s[2] + s[3] + s[4]) / 3
        if per > top_per:
            top_per = per
            top_name = s[1]
    print("Class Topper:", top_name, "with", round(top_per,2), "%")

def main_menu():
    while True:
        print("\n=== STUDENT MANAGEMENT SYSTEM ===")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student")
        print("4. Show Class Topper")
        print("5. Exit")

        ch = int(input("Enter choice: "))

        if ch == 1:
            add_student()
        elif ch == 2:
            display_all()
        elif ch == 3:
            search_student()
        elif ch == 4:
            class_toppers()
        elif ch == 5:
            print("Thank you!")
            break
        else:
            print("Invalid choice")

main_menu()