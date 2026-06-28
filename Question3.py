# Program to count vowels and consonants
s = input("Enter a string: ")

vowels = 0
consonants = 0
s = s.lower() 

for i in s:
    if i >= 'a' and i <= 'z':
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            vowels = vowels + 1
        else:
            consonants = consonants + 1

print("Vowels:", vowels)
print("Consonants:", consonants)