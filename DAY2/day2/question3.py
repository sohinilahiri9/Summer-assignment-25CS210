num = int(input("Enter a number: "))
temp = abs(num)
product = 1

if temp == 0:
    product = 0
else:
    while temp > 0:
        product *= temp % 10
        temp //= 10

print(f"Product of digits of {num} = {product}")