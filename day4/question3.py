num = int(input("Enter a number: "))
temp = num
sum_digits = 0

while temp > 0:
    digit = temp % 10
    sum_digits += digit ** 3
    temp //= 10

if num == sum_digits:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")