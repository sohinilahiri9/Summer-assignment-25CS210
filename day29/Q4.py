# Inventory Management System
inventory = [] 

while True:
    print("\n--- INVENTORY MANAGEMENT ---")
    print("1. Add Item")
    print("2. View All Items")
    print("3. Update Quantity")
    print("4. Delete Item")
    print("5. Calculate Total Stock Value")
    print("6. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        item_id = int(input("Enter item ID: "))
        name = input("Enter item name: ")
        qty = int(input("Enter quantity: "))
        price = float(input("Enter price: "))
        inventory.append([item_id, name, qty, price])
        print("Item added to inventory")

    elif ch == 2:
        print("\nID\tName\t\tQty\tPrice")
        for item in inventory:
            print(item[0], "\t", item[1], "\t", item[2], "\t", item[3])

    elif ch == 3:
        item_id = int(input("Enter item ID to update: "))
        for item in inventory:
            if item[0] == item_id:
                new_qty = int(input("Enter new quantity: "))
                item[2] = new_qty
                print("Quantity updated")
                break
        else:
            print("Item not found")

    elif ch == 4:
        item_id = int(input("Enter item ID to delete: "))
        for item in inventory:
            if item[0] == item_id:
                inventory.remove(item)
                print("Item deleted")
                break
        else:
            print("Item not found")

    elif ch == 5:
        total = 0
        for item in inventory:
            total = total + (item[2] * item[3])
        print("Total Inventory Value:", total)

    elif ch == 6:
        print("Exiting...")
        break
    else:
        print("Invalid choice")