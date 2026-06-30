# Mini Employee Management System
emp_id = []
emp_name = []
emp_dept = []
emp_salary = []

while True:
    print("\n--- EMPLOYEE MANAGEMENT ---")
    print("1. Add Employee")
    print("2. View All Employees")
    print("3. Update Salary")
    print("4. Delete Employee")
    print("5. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        eid = int(input("Enter ID: "))
        ename = input("Enter name: ")
        edept = input("Enter department: ")
        esal = int(input("Enter salary: "))
        emp_id.append(eid)
        emp_name.append(ename)
        emp_dept.append(edept)
        emp_salary.append(esal)
        print("Employee added")

    elif ch == 2:
        print("\nID\tName\t\tDept\tSalary")
        for i in range(len(emp_id)):
            print(emp_id[i], "\t", emp_name[i], "\t", emp_dept[i], "\t", emp_salary[i])

    elif ch == 3:
        eid = int(input("Enter ID to update: "))
        for i in range(len(emp_id)):
            if emp_id[i] == eid:
                new_sal = int(input("Enter new salary: "))
                emp_salary[i] = new_sal
                print("Salary updated")
                break
        else:
            print("Employee not found")

    elif ch == 4:
        eid = int(input("Enter ID to delete: "))
        for i in range(len(emp_id)):
            if emp_id[i] == eid:
                emp_id.pop(i)
                emp_name.pop(i)
                emp_dept.pop(i)
                emp_salary.pop(i)
                print("Employee deleted")
                break
        else:
            print("Employee not found")

    elif ch == 5:
        break
    else:
        print("Invalid choice")