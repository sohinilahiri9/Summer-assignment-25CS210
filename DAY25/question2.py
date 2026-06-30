s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

common = ""
for i in s1:
    for j in s2:
        if i == j:
            flag = 0
            
            for k in common:
                if i == k:
                    flag = 1
                    break
            if flag == 0:
                common = common + i
            break

print("Common characters:", common)