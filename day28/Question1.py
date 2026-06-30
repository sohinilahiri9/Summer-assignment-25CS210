# Library Management System
books = [] # [book_id, title, author, status]
book_id = 100

while True:
    print("\n--- Library Management ---")
    print("1. Add Book")
    print("2. Display All Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        title = input("Enter book title: ")
        author = input("Enter author: ")
        books.append([book_id, title, author, "Available"])
        print("Book added with ID:", book_id)
        book_id = book_id + 1

    elif ch == 2:
        print("\nID\tTitle\t\tAuthor\t\tStatus")
        for b in books:
            print(b[0], "\t", b[1], "\t", b[2], "\t", b[3])

    elif ch == 3:
        bid = int(input("Enter book ID to issue: "))
        for b in books:
            if b[0] == bid:
                if b[3] == "Available":
                    b[3] = "Issued"
                    print("Book issued successfully")
                else:
                    print("Book already issued")
                break
        else:
            print("Book not found")

    elif ch == 4:
        bid = int(input("Enter book ID to return: "))
        for b in books:
            if b[0] == bid:
                if b[3] == "Issued":
                    b[3] = "Available"
                    print("Book returned successfully")
                else:
                    print("Book was not issued")
                break
        else:
            print("Book not found")

    elif ch == 5:
        break
    else:
        print("Invalid choice")