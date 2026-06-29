# Frequency count program
n = int(input("Enter size of array: "))

arr = []
for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

key = int(input("Enter element to count: "))

count = 0
for i in arr:
    if i == key:
        count = count + 1

print(key, "appears", count, "times")