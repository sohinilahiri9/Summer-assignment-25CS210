# Program to find common elements
n1 = int(input("Size of first array: "))
arr1 = []
for i in range(n1):
    arr1.append(int(input()))

n2 = int(input("Size of second array: "))
arr2 = []
for i in range(n2):
    arr2.append(int(input()))

print("Common elements are:")

for i in range(n1):
    for j in range(n2):
        if arr1[i] == arr2[j]:
            print(arr1[i])
            break