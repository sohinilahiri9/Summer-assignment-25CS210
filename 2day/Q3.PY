num = int(input("Enter a number: "))
temp = num
product = 1

if num == 0:
    product = 0
else:
    while num > 0:
        digit = num % 10
        product *= digit
        num //= 10

print(f"Product of digits of {temp} = {product}")