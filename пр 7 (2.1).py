import math
def s(a):
    s = a*a*math.sqrt(3)/4
    return s
print("Введите сторону шестиугольника")
a = int(input("a: "))
print("Площадь шестиугольника: ",s(a)*6)
