# Program to reverse string
s = input("Enter a string: ")

rev = ""
for i in s:
    rev = i + rev # add new char at start

print("Reversed string:", rev)