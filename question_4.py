n = int(input("Enter number: "))
count = 0
temp = n

while temp > 0:
    count += 1
    temp //= 10  

print(f"Number of digit in {n} = {count}")