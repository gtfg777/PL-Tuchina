a = list(map(int, input("Введите список целых чисел: ").split()))
b = []
c = []
for x in a:
    if (x > 0) :
        b.append(x)
    else:
        c.append(x)
print("Список положительных чисел: ",b)
print("Список отрицательных чисел: ",c)




