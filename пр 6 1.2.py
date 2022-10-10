a = list(map(float, input("Введите список: ").split()))
t = sum(a) / len(a)
for i in range(len(a)):
    if a[i] == 0:
        a[i] = t
        print(a, end=" ")
