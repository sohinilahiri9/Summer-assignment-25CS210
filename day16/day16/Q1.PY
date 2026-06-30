
# Program to find missing number
n = int(input("Enter size of array: "))

arr = []
for i in range(n):
    arr.append(int(input("Enter element: ")))

print("Array:", arr)

total = (n + 1) * (n + 2) // 2
arr_sum = 0

for i in arr:
    arr_sum = arr_sum + i

missing = total - arr_sum
print("Missing number =", missing)