# Program to check symmetric matrix
n = int(input("Enter size of square matrix: "))

mat = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(int(input()))
    mat.append(row)

symmetric = True
for i in range(n):
    for j in range(n):
        if mat[i][j]!= mat[j][i]:
            symmetric = False
            break

if symmetric == True:
    print("Matrix is symmetric")
else:
    print("Matrix is not symmetric")