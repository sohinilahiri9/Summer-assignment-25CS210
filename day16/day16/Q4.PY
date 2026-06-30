# Program to remove duplicates
n = int(input("Enter size of array: "))

arr = []
for i in range(n):
    arr.append(int(input("Enter element: ")))

print("Original array:", arr)

new_arr = []
for i in range(n):
    if arr[i] not in new_arr:
        new_arr.append(arr[i])

print("Array after removing duplicates:", new_arr)