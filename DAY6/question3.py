n = int(input("Enter number: "))
count = 0
temp = n

while temp > 0:
    count += temp % 2
    temp = temp // 2
    
print(f"Set bits in {n} = {count}")