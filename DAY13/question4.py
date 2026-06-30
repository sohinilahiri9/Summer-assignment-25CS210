# Program to count even and odd
n = int(input("Enter size of array: "))

arr = []
for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

even = 0
odd = 0

for i in arr:
    if i % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1

print("Array:", arr)
print("Even count =", even)
print("Odd count =", odd)