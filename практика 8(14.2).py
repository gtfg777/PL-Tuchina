n = int(input("Enter the value of the matrix: "))
mattrix = [[0]*n for i in range(n)]
a, b = 1, 0

mattrix[n//2][n//2]=n*n           #центр матрицы
for v in range(n//2):             #верхняя горизонталь матрицы
    for i in range(n-b):
        mattrix[v][i+v] = a
        a+=1
    for i in range(v+1, n-v):      #правая вертикаль матрицы
        mattrix[i][-v-1] = a
        a+=1
    for i in range(v+1, n-v):      #нижняя горизонталь матрицы
        mattrix[-v-1][-i-1] =a
        a+=1
    for i in range(v+1, n-(v+1)):  #левая вертикаль матрицы
        mattrix[-i-1][v]=a
        a+=1
    b+=2
for i in mattrix:
    print(*i)
