# Program to remove duplicate characters
s = input("Enter a string: ")

result = ""
for i in s:
    flag = 0
    for j in result:
        if i == j:
            flag = 1
            break
    if flag == 0:
        result = result + i

print("String after removing duplicates:", result)