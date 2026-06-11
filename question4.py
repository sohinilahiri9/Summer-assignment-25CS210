start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

print(f"Armstrong numbers between {start} and {end}:")
for num in range(start, end + 1):
    temp = num
    sum_digits = 0
    
    while temp > 0:
        digit = temp % 10
        sum_digits += digit ** 3
        temp //= 10
    
    if num == sum_digits:
        print(num, end=" ")