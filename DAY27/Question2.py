# Employee Management System
employees = [] # [id, name, dept, salary]

while True:
    print("\n--- Employee Management ---")
    print("1. Add Employee")
    print("2. View All Employees")
    print("3. Update Salary")
    print("4. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        eid = int(input("Enter ID: "))
        name = input("Enter name: ")
        dept = input("Enter department: ")
        sal = int(input("Enter salary: "))
        employees.append([eid, name, dept, sal])
        print("Employee added")

    elif ch == 2:
        print("\nID\tName\tDept\tSalary")
        for e in employees:
            print(e[0], "\t", e[1], "\t", e[2], "\t", e[3])

    elif ch == 3:
        eid = int(input("Enter ID to update salary: "))
        for e in employees:
            if e[0] == eid:
                new_sal = int(input("Enter new salary: "))
                e[3] = new_sal
                print("Salary updated")
                break
        else:
            print("Employee not found")

    elif ch == 4:
        break

    else:
        print("Invalid choice")