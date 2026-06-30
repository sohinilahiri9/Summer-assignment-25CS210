# Program to subtract matrices
r = int(input("Enter rows: "))
c = int(input("Enter columns: "))

mat1 = []
for i in range(r):
    row = []
    for j in range(c):
        row.append(int(input("Mat1 element: ")))
    mat1.append(row)

mat2 = []
for i in range(r):
    row = []
    for j in range(c):
        row.append(int(input("Mat2 element: ")))
    mat2.append(row)

diff = []
for i in range(r):
    row = []
    for j in range(c):
        row.append(mat1[i][j] - mat2[i][j])
    diff.append(row)

print("Difference:")
for i in range(r):
    print(diff[i])