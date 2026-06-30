# Program to move all 0's to end
n = int(input("Enter size of array: "))

arr = []
for i in range(n):
    arr.append(int(input("Enter element: ")))

print("Original array:", arr)

count = 0 

for i in range(n):
    if arr[i]!= 0:
        arr[count] = arr[i]
        count = count + 1

while count < n:
    arr[count] = 0
    count = count + 1

print("Array after moving zeroes:", arr)