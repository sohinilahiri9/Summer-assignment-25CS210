# Menu-driven Array Operations
arr = []

while True:
    print("\n--- ARRAY OPERATIONS ---")
    print("1. Insert element")
    print("2. Delete element")
    print("3. Search element")
    print("4. Display array")
    print("5. Find max and min")
    print("6. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        ele = int(input("Enter element to insert: "))
        arr.append(ele)
        print("Element inserted")

    elif ch == 2:
        ele = int(input("Enter element to delete: "))
        if ele in arr:
            arr.remove(ele)
            print("Element deleted")
        else:
            print("Element not found")

    elif ch == 3:
        ele = int(input("Enter element to search: "))
        flag = 0
        for i in range(len(arr)):
            if arr[i] == ele:
                print("Element found at index", i)
                flag = 1
                break
        if flag == 0:
            print("Element not found")

    elif ch == 4:
        print("Array:", arr)

    elif ch == 5:
        if len(arr) == 0:
            print("Array is empty")
        else:
            max_val = arr[0]
            min_val = arr[0]
            for i in arr:
                if i > max_val:
                    max_val = i
                if i < min_val:
                    min_val = i
            print("Max:", max_val, "Min:", min_val)

    elif ch == 6:
        break
    else:
        print("Invalid choice")