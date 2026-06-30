b = input("Enter binary number: ")
decimal = 0
power = 0

for digit in reversed(b):
    if digit == '1':
        decimal += 2 ** power
    power += 1
    
print(f"Decimal of {b} = {decimal}")