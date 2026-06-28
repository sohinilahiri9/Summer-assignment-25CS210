num = int(input("Enter number: "))

print(f"Multiplication table of {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")