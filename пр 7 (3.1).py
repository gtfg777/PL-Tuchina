import math
def c(a,b):
    c = math.sqrt(a*a+b*b)
    return c
A = []
for i in range(2):
    print("Введите катеты треугольника",i)
    a = int(input("a: "))
    b = int(input("b: "))
    A.append(c(a,b))
for i in range(2):
    print("Гипотенуза треугольника",i," =  {:.2f}".format(A[i]))
if(A[1]>A[0]):
    print("Гипотенуза 1 - го  треугольника больше гипотенузы 0 - го треугольника")
elif(A[1]<A[0]):
    print("Гипотенуза 0 - го  треугольника больше гипотенузы 1 - го треугольника")
else:
    print("Гипотенузы равны")
