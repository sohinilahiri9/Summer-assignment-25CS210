r = int(input())
for i in range(1, r+1):
    a = ""
    for j in range(1, i+1):
        a = a + chr(64+j)
    for k in range(i-1, 0, -1):
        a = a + chr(64+k)
    print(" "*(r-i) + a)