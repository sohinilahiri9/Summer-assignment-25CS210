# Program to convert lowercase to uppercase
s = input("Enter lowercase string: ")

upper_str = ""
for i in s:
    if i >= 'a' and i <= 'z':

        upper_str = upper_str + chr(ord(i) - 32)
    else:
        upper_str = upper_str + i

print("Uppercase string:", upper_str)