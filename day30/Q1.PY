# Student Record System using Arrays and Strings
roll = []
name = []
marks = []

while True:
    print("\n--- STUDENT RECORD SYSTEM ---")
    print("1. Add Student")
    print("2. Display All")
    print("3. Search by Roll")
    print("4. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        r = int(input("Enter roll no: "))
        n = input("Enter name: ")
        m = int(input("Enter marks: "))
        roll.append(r)
        name.append(n)
        marks.append(m)
        print("Student added")

    elif ch == 2:
        print("\nRoll\tName\t\tMarks")
        for i in range(len(roll)):
            print(roll[i], "\t", name[i], "\t", marks[i])

    elif ch == 3:
        r = int(input("Enter roll to search: "))
        found = 0
        for i in range(len(roll)):
            if roll[i] == r:
                print("Found:", name[i], "Marks:", marks[i])
                found = 1
                break
        if found == 0:
            print("Student not found")

    elif ch == 4:
        break
    else:
        print("Invalid choice")