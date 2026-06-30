# Ticket Booking System
seats = [0] * 10 

while True:
    print("\n--- Movie Ticket Booking ---")
    print("1. View Seats")
    print("2. Book Seat")
    print("3. Cancel Booking")
    print("4. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        print("\nSeat Status: 0=Available, 1=Booked")
        for i in range(10):
            print("Seat", i+1, ":", seats[i])

    elif ch == 2:
        s_no = int(input("Enter seat number 1-10: "))
        if s_no >= 1 and s_no <= 10:
            if seats[s_no-1] == 0:
                seats[s_no-1] = 1
                print("Seat", s_no, "booked successfully")
            else:
                print("Seat already booked")
        else:
            print("Invalid seat number")

    elif ch == 3:
        s_no = int(input("Enter seat number to cancel 1-10: "))
        if s_no >= 1 and s_no <= 10:
            if seats[s_no-1] == 1:
                seats[s_no-1] = 0
                print("Booking cancelled for seat", s_no)
            else:
                print("Seat was not booked")
        else:
            print("Invalid seat number")

    elif ch == 4:
        break
    else:
        print("Invalid choice")