# Program to input and display array
n = int(input("Enter size of array: "))

arr = []
print("Enter", n, "elements:")

for i in range(n):
    num = int(input())
    arr.append(num)

print("Array is:", arr)