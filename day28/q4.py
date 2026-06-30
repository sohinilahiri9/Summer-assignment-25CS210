# Contact Management System
contacts = [] 

while True:
    print("\n--- Contact Management ---")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")
        contacts.append([name, phone, email])
        print("Contact saved")

    elif ch == 2:
        print("\nName\t\tPhone\t\tEmail")
        for c in contacts:
            print(c[0], "\t", c[1], "\t", c[2])

    elif ch == 3:
        s_name = input("Enter name to search: ")
        found = 0
        for c in contacts:
            if c[0].lower() == s_name.lower():
                print("Found:", c[0], c[1], c[2])
                found = 1
        if found == 0:
            print("Contact not found")

    elif ch == 4:
        d_name = input("Enter name to delete: ")
        for c in contacts:
            if c[0].lower() == d_name.lower():
                contacts.remove(c)
                print("Contact deleted")
                break
        else:
            print("Contact not found")

    elif ch == 5:
        print("Exiting...")
        break
    else:
        print("Invalid choice")