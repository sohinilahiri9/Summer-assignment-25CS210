# Menu-driven String Operations
s = input("Enter a string: ")

while True:
    print("\n--- STRING OPERATIONS ---")
    print("1. Find length")
    print("2. Reverse string")
    print("3. Check palindrome")
    print("4. Count vowels")
    print("5. Change string")
    print("6. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        count = 0
        for i in s:
            count = count + 1
        print("Length of string:", count)

    elif ch == 2:
        rev = ""
        for i in s:
            rev = i + rev
        print("Reversed string:", rev)

    elif ch == 3:
        rev = ""
        for i in s:
            rev = i + rev
        if s == rev:
            print("String is palindrome")
        else:
            print("String is not palindrome")

    elif ch == 4:
        v_count = 0
        for i in s:
            if i in 'aeiouAEIOU':
                v_count = v_count + 1
        print("Total vowels:", v_count)

    elif ch == 5:
        s = input("Enter new string: ")
        print("String updated")

    elif ch == 6:
        break
    else:
        print("Invalid choice")