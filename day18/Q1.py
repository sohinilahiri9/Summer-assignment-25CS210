# Program for bubble sort - ascending
n = int(input("Enter size of array: "))

arr = []
for i in range(n):
    arr.append(int(input("Enter element: ")))

print("Original array:", arr)

for i in range(n-1):
    for j in range(0, n-i-1):
        if arr[j] > arr[j+1]:
            # swap
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp

print("Sorted array:", arr)