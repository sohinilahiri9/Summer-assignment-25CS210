
num = int(input("Enter a number: "))

temp = num

reverse = 0

while num > 0:

digit = num % 10

2

reverse = reverse * 10 + digit

num //= 10

print(f"Reverse of {temp} = {reverse}")