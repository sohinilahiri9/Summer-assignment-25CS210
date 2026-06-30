# Program to merge 2 arrays
print("Enter first array")
n1 = int(input("Size: "))

arr1 = []
for i in range(n1):
    arr1.append(int(input("Element: ")))

print("Enter second array")
n2 = int(input("Size: "))

arr2 = []
for i in range(n2):
    arr2.append(int(input("Element: ")))

merged = []
for i in range(n1):
    merged.append(arr1[i])
for i in range(n2):
    merged.append(arr2[i])

print("Merged array:", merged)