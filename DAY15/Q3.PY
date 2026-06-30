
# Program to rotate right by 1
n = int(input("Enter size of array: "))

arr = []
for i in range(n):
    arr.append(int(input("Enter element: ")))

print("Original array:", arr)

last = arr[n-1]

for i in range(n-1, 0, -1):
    arr[i] = arr[i-1]

arr[0] = last

print("Right rotated array:", arr)