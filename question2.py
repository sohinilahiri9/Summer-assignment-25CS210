# Program to compress string
s = input("Enter a string: ")

compress = ""
i = 0
while i < len(s):
    count = 1
    while i + 1 < len(s) and s[i] == s[i+1]:
        count = count + 1
        i = i + 1
    compress = compress + s[i] + str(count)
    i = i + 1

print("Compressed string:", compress)