# Program to remove spaces from string
s = input("Enter a string: ")

new_str = ""
for i in s:
    if i != ' ': # skip space character
        new_str = new_str + i

print("String without spaces:", new_str)