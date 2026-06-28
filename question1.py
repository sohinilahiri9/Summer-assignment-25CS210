# Program to check if s2 is rotation of s1

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if len(s1)!= len(s2):
    print("Not rotation")
else:
    temp = s1 + s1 
    flag = 0
    for i in range(len(temp) - len(s2) + 1):
        if temp[i:i+len(s2)] == s2:
            flag = 1
            break

    if flag == 1:
        print("Strings are rotations of each other")
    else:
        print("Not rotation")