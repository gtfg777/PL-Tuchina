import random
def change(matrix,m,i):
    matrix[m],matrix[i] = matrix[i],matrix[m]
    return matrix
n = int(input("Enter the value of the matrix: "))
matrix = [[random.randint(1,10) for i in range(n)]for j in range(n)]
max = 0
d_row = 0
for i in range(n):                                             #поиск максимума на главной диагонали
    for j in range(n):
        if(matrix[i][i]>max):
            max=matrix[i][i]
            d_row = i
for i in range(n):
    print(matrix[i])
print("Max is",max)
print("row with max is",d_row)
print("!!!!!Warning row must be < or = value of the matrix!!!!! ")
m = int(input("Enter row: "))                                   #работа с новой строкой
for c in range(n):
    if(m>n and m == n and m<0):
        print("Error! Try again")
    else:
        matrix == (change(matrix,m, i))
for k in matrix:
    print(k)
