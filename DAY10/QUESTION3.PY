r = int(input())
for i in range(1, r+1):
    a = ""
    for j in range(1, i+1):
        a = a + str(j)
    for k in range(i-1, 0, -1):
        a = a + str(k)
    print(" "*(r-i) + a)