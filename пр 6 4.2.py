a = list(map(int, input("Введите список чисел: ").split()))
b = []
for i in a:
    if(i%2!=0):
        b.append(i)
if(len(b) == 0):
    print("Нечетных чисел в массиве нет")

b.sort(reverse=True)
print(b)