# Program for character frequency
s = input("Enter a string: ")

for i in s:
    if i!= ' ': 
        count = 0
        for j in s:
            if i == j:
                count = count + 1
        print(i, ":", count)