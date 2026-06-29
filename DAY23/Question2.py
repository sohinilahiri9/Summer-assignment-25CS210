# Program to find first repeating character
s = input("Enter a string: ")

flag = 0
for i in range(len(s)):
    for j in range(i + 1, len(s)):
        if s[i] == s[j]:
            print("First repeating character:", s[i])
            flag = 1
            break
    if flag == 1:
        break

if flag == 0:
    print("No repeating character found")