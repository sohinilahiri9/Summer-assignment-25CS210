# Program to check palindrome string
s = input("Enter a string: ")

rev = ""
for i in s:
    rev = i + rev 

if s == rev:
    print("Palindrome string")
else:
    print("Not a palindrome string")