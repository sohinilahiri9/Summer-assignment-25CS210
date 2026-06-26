
# Program to find longest word in sentence
s = input("Enter a sentence: ")

max_len = 0
longest = ""
word = ""

for i in s:
    if i!= ' ':
        word = word + i
    else:
        if len(word) > max_len:
            max_len = len(word)
            longest = word
        word = ""

# check last word
if len(word) > max_len:
    longest = word

print("Longest word:", longest)