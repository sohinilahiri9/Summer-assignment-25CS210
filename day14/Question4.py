# Find duplicates program
n = int(input("Enter size of array: "))

arr = []
for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

print("Array:", arr)
print("Duplicate elements are:")

# Use sets to track elements and duplicates
seen = set()
duplicates = set()

for num in arr:
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)

# Print unique duplicates
for item in duplicates:
    print(item)