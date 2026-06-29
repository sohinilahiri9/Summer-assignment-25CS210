# Linear search program
n = int(input("Enter size of array: "))

arr = []
for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

key = int(input("Enter element to search: "))

found = False
for i in range(n):
    if arr[i] == key:
        print(key, "found at index", i)
        found = True
        break

if found == False:
    print(key, "not found in array")