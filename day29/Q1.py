# Menu-driven Calculator
while True:
    print("\n--- CALCULATOR ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    ch = int(input("Enter choice: "))

    if ch == 5:
        print("Exiting calculator...")
        break

    if ch >= 1 and ch <= 4:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if ch == 1:
            print("Result:", a + b)
        elif ch == 2:
            print("Result:", a - b)
        elif ch == 3:
            print("Result:", a * b)
        elif ch == 4:
            if b!= 0:
                print("Result:", a / b)
            else:
                print("Error: Cannot divide by zero")
    else:
        print("Invalid choice")