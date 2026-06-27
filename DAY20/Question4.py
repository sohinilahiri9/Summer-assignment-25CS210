# Program for column-wise sum
r = int(input("Enter rows: "))
c = int(input("Enter columns: "))

mat = []
for i in range(r):
    row = []
    for j in range(c):
        row.append(int(input()))
    mat.append(row)

print("Column-wise sum:")
for j in range(c):
    sum = 0
    for i in range(r):
        sum = sum + mat[i][j]
    print("Column", j+1, "sum =", sum)