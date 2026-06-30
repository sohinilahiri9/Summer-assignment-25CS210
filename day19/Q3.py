# Program for transpose
r = int(input("Enter rows: "))
c = int(input("Enter columns: "))

mat = []
for i in range(r):
    row = []
    for j in range(c):
        row.append(int(input()))
    mat.append(row)

print("Original matrix:")
for i in range(r):
    print(mat[i])

transpose = []
for i in range(c):
    row = []
    for j in range(r):
        row.append(mat[j][i])
    transpose.append(row)

print("Transpose matrix:")
for i in range(c):
    print(transpose[i])