# Program for row-wise sum
r = int(input("Enter rows: "))
c = int(input("Enter columns: "))

mat = []
for i in range(r):
    row = []
    for j in range(c):
        row.append(int(input()))
    mat.append(row)

print("Row-wise sum:")
for i in range(r):
    sum = 0
    for j in range(c):
        sum = sum + mat[i][j]
    print("Row", i+1, "sum =", sum)