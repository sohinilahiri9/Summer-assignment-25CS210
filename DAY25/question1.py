# Program to merge two sorted arrays
n1 = int(input("Enter size of first array: "))
arr1 = []
print("Enter elements of first sorted array:")
for i in range(n1):
    arr1.append(int(input()))

n2 = int(input("Enter size of second array: "))
arr2 = []
print("Enter elements of second sorted array:")
for i in range(n2):
    arr2.append(int(input()))

merged = []
i = 0
j = 0

while i < n1 and j < n2:
    if arr1[i] < arr2[j]:
        merged.append(arr1[i])
        i = i + 1
    else:
        merged.append(arr2[j])
        j = j + 1

while i < n1:
    merged.append(arr1[i])
    i = i + 1
while j < n2:
    merged.append(arr2[j])
    j = j + 1

print("Merged array:", merged)