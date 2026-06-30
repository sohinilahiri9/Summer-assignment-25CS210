# Program to find element with max frequency
n = int(input("Enter size of array: "))

arr = []
for i in range(n):
    arr.append(int(input("Enter element: ")))

print("Array:", arr)

max_count = 0
max_ele = arr[0]

for i in range(n):
    count = 0
    for j in range(n):
        if arr[i] == arr[j]:
            count = count + 1

    if count > max_count:
        max_count = count
        max_ele = arr[i]

print("Element with max frequency:", max_ele)
print("Frequency =", max_count)