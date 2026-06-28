# Program for maximum occurring character
s = input("Enter a string: ")

max_count = 0
max_char = ''

for i in s:
    if i!= ' ': 
        count = 0
        for j in s:
            if i == j:
                count = count + 1
        if count > max_count:
            max_count = count
            max_char = i

if max_char!= '':
    print("Maximum occurring character:", max_char)
    print("Count:", max_count)
else:
    print("No characters found")