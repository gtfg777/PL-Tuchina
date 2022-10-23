def s(a,b):
    s = a*b
    return s
A = []
for i in range(3):
    print("Введите стороны прямоугольника",i)
    a = int(input("a: "))
    b = int(input("b: "))
    A.append(s(a,b))
for i in range(3):
    print("Площадь прямоугольника",i," =  {:.2f}".format(A[i]))
