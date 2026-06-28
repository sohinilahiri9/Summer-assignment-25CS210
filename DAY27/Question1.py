# Student Record Management System
students = [] # stores [roll, name, marks]

while True:
    print("\n--- Student Record System ---")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        roll = int(input("Enter roll no: "))
        name = input("Enter name: ")
        marks = int(input("Enter marks: "))
        students.append([roll, name, marks])
        print("Student added successfully")

    elif choice == 2:
        print("\nRoll\tName\tMarks")
        for s in students:
            print(s[0], "\t", s[1], "\t", s[2])

    elif choice == 3:
        r = int(input("Enter roll no to search: "))
        found = 0
        for s in students:
            if s[0] == r:
                print("Found:", s[1], "Marks:", s[2])
                found = 1
                break
        if found == 0:
            print("Student not found")

    elif choice == 4:
        r = int(input("Enter roll no to delete: "))
        for s in students:
            if s[0] == r:
                students.remove(s)
                print("Student deleted")
                break
        else:
            print("Student not found")

    elif choice == 5:
        print("Exiting...")
        break

    else:
        print("Invalid choice")