# Bank Account System
account_no = 1001
balance = 0
name = ""

while True:
    print("\n--- Bank Account System ---")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        name = input("Enter account holder name: ")
        balance = 0
        print("Account created successfully")
        print("Account No:", account_no)
        print("Initial Balance: 0")

    elif ch == 2:
        amt = int(input("Enter amount to deposit: "))
        if amt > 0:
            balance = balance + amt
            print("Deposited successfully")
            print("New Balance:", balance)
        else:
            print("Invalid amount")

    elif ch == 3:
        amt = int(input("Enter amount to withdraw: "))
        if amt <= balance and amt > 0:
            balance = balance - amt
            print("Withdrawal successful")
            print("Remaining Balance:", balance)
        else:
            print("Insufficient balance or invalid amount")

    elif ch == 4:
        print("Account Holder:", name)
        print("Account No:", account_no)
        print("Current Balance:", balance)

    elif ch == 5:
        print("Thank you for using our bank")
        break
    else:
        print("Invalid choice")