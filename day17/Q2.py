# Program for union
n1 = int(input("Size of first array: "))
arr1 = []
for i in range(n1):
    arr1.append(int(input()))

n2 = int(input("Size of second array: "))
arr2 = []
for i in range(n2):
    arr2.append(int(input()))

union = []

for i in range(n1):
    if arr1[i] not in union:
        union.append(arr1[i])

for i in range(n2):
    if arr2[i] not in union:
        union.append(arr2[i])

print("Union of arrays:", union)