# Mini Library System
book_id = []
title = []
author = []
status = [] 

while True:
    print("\n--- MINI LIBRARY ---")
    print("1. Add Book")
    print("2. Show All Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        bid = int(input("Enter book ID: "))
        btitle = input("Enter title: ")
        bauthor = input("Enter author: ")
        book_id.append(bid)
        title.append(btitle)
        author.append(bauthor)
        status.append("Available")
        print("Book added")

    elif ch == 2:
        print("\nID\tTitle\t\tAuthor\t\tStatus")
        for i in range(len(book_id)):
            print(book_id[i], "\t", title[i], "\t", author[i], "\t", status[i])

    elif ch == 3:
        bid = int(input("Enter book ID to issue: "))
        for i in range(len(book_id)):
            if book_id[i] == bid:
                if status[i] == "Available":
                    status[i] = "Issued"
                    print("Book issued to you")
                else:
                    print("Book already issued")
                break
        else:
            print("Book ID not found")

    elif ch == 4:
        bid = int(input("Enter book ID to return: "))
        for i in range(len(book_id)):
            if book_id[i] == bid:
                if status[i] == "Issued":
                    status[i] = "Available"
                    print("Book returned")
                else:
                    print("Book was not issued")
                break
        else:
            print("Book ID not found")

    elif ch == 5:
        break
    else:
        print("Invalid choice")