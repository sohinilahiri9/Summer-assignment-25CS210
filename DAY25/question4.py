# Program to sort words by length
s = input("Enter a sentence: ")

words = []
word = ""
for i in s:
    if i!= ' ':
        word = word + i
    else:
        if word!= "":
            words.append(word)
            word = ""
if word!= "":
    words.append(word)

n = len(words)
for i in range(n):
    for j in range(0, n-i-1):
        if len(words[j]) > len(words[j+1]):
            temp = words[j]
            words[j] = words[j+1]
            words[j+1] = temp

print("Words sorted by length:")
for w in words:
    print(w, end=' ')