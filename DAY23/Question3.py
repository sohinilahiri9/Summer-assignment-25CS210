# Program to check anagram strings
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

# convert to lowercase and remove spaces
str1 = ""
str2 = ""
for i in s1:
    if i!= ' ':
        str1 = str1 + i.lower()
for i in s2:
    if i!= ' ':
        str2 = str2 + i.lower()

# check length first
if len(str1)!= len(str2):
    print("Not anagram")
else:
    # check frequency of each character
    is_anagram = 1
    for ch in str1:
        c1 = 0
        c2 = 0
        for x in str1:
            if ch == x:
                c1 = c1 + 1
        for y in str2:
            if ch == y:
                c2 = c2 + 1
        if c1!= c2:
            is_anagram = 0
            break

    if is_anagram == 1:
        print("Anagram strings")
    else:
        print("Not anagram")