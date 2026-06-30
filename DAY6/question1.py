n = int(input("Enter decimal number: "))

if n == 0:
    print("Binary: 0")
else:
    binary = ""
    temp = n
    while temp > 0:
        binary = str(temp % 2) + binary
        temp = temp // 2
    print(f"Binary of {n} = {binary}")