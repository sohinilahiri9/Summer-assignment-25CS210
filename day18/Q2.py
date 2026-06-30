# Program for selection sort
n = int(input("Enter size of array: "))

arr = []
for i in range(n):
    arr.append(int(input("Enter element: ")))

print("Original array:", arr)

for i in range(n):
    min_index = i
    for j in range(i+1, n):
        if arr[j] < arr[min_index]:
            min_index = j

    temp = arr[i]
    arr[i] = arr[min_index]
    arr[min_index] = temp

print("Sorted array:", arr)