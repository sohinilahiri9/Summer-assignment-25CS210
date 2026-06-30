# Program to sort names alphabetically
n = int(input("Enter number of names: "))
names = []
print("Enter names:")
for i in range(n):
    names.append(input())

for i in range(n):
    for j in range(0, n-i-1):
        if names[j] > names[j+1]:
            temp = names[j]
            names[j] = names[j+1]
            names[j+1] = temp

print("Names in alphabetical order:")
for name in names:
    print(name)