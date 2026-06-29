# Program to find sum and average
n = int(input("Enter size of array: "))

arr = []
for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

sum = 0
for i in arr:
    sum = sum + i

avg = sum / n

print("Array:", arr)
print("Sum =", sum)
print("Average =", avg)