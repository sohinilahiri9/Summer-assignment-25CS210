# Program for binary search
n = int(input("Enter size of sorted array: "))

arr = []
for i in range(n):
    arr.append(int(input("Enter element: ")))

key = int(input("Enter element to search: "))

low = 0
high = n - 1
found = False

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == key:
        print("Element found at position", mid+1)
        found = True
        break
    elif arr[mid] < key:
        low = mid + 1
    else:
        high = mid - 1

if found == False:
    print("Element not found")