def sum_digits(n):
    if n == 0:  # base case
        return 0
    return n % 10 + sum_digits(n // 10)  # last digit + rest

num = int(input("Enter number: "))
print(f"Sum of digits of {num} = {sum_digits(num)}")