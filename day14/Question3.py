# Second largest program
n = int(input("Enter size of array: "))

arr = []
for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

first = second = arr[0]

for i in arr:
    if i > first:
        second = first
        first = i
    elif i > second and i!= first:
        second = i

print("Array:", arr)
print("Largest =", first)
print("Second Largest =", second)