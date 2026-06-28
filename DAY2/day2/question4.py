num = int(input("Enter a number: "))
temp = abs(num)
reverse = 0
original = temp

while temp > 0:
    reverse = reverse * 10 + temp % 10
    temp //= 10

if original == reverse:
    print(f"{num} is a palindrome")
else:
    print(f"{num} is not a palindrome")