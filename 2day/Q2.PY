num = int(input("Enter a number: "))
temp = num
sum_digits = 0

while num > 0:
    digit = num % 10
    sum_digits += digit
    num //= 10

print(f"Sum of digits of {temp} = {sum_digits}")