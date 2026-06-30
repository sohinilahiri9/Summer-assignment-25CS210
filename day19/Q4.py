# Program for diagonal sum
n = int(input("Enter size of square matrix: "))

mat = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(int(input()))
    mat.append(row)

sum1 = 0 # main diagonal
sum2 = 0 # other diagonal

for i in range(n):
    sum1 = sum1 + mat[i][i]
    sum2 = sum2 + mat[i][n-i-1]

print("Main diagonal sum:", sum1)
print("Other diagonal sum:", sum2)
print("Total diagonal sum:", sum1 + sum2)