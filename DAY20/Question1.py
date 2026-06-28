# Program to multiply 2 matrices
r1 = int(input("Rows of first matrix: "))
c1 = int(input("Cols of first matrix: "))

mat1 = []
for i in range(r1):
    row = []
    for j in range(c1):
        row.append(int(input("Mat1 element: ")))
    mat1.append(row)

r2 = int(input("Rows of second matrix: "))
c2 = int(input("Cols of second matrix: "))

mat2 = []
for i in range(r2):
    row = []
    for j in range(c2):
        row.append(int(input("Mat2 element: ")))
    mat2.append(row)

if c1!= r2:
    print("Multiplication not possible")
else:
    result = []
    for i in range(r1):
        row = []
        for j in range(c2):
            sum = 0
            for k in range(c1):
                sum = sum + mat1[i][k] * mat2[k][j]
            row.append(sum)
        result.append(row)

    print("Result:")
    for i in range(r1):
        print(result[i])