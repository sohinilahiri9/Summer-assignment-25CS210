# Program to find pair with given sum
n = int(input("Enter size of array: "))

arr = []
for i in range(n):
    arr.append(int(input("Enter element: ")))

sum = int(input("Enter target sum: "))

print("Array:", arr)
print("Pairs with sum", sum, ":")

found = False
for i in range(n):
    for j in range(i+1, n):
        if arr[i] + arr[j] == sum:
            print(arr[i], "+", arr[j])
            found = True

if found == False:
    print("No pair found")