a = list(map(float, input("Введите список из 10 целых чисел: ").split()))
b = []
for i in a:
    if(i>5):
        b.append(i)
        d = sum(b)
print(d)
