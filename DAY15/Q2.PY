# Program to rotate left by 1
n = int(input("Enter size of array: "))
arr = []
for i in range(n):
    arr.append(int(input("Enter element: ")))
print("Original array:", arr)
first = arr[0]
for i in range(0, n-1):
    arr[i] = arr[i+1]
arr[n-1] = first
print("Left rotated array:", arr)