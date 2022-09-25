f = float(input('Введите первое число: '))
k = float(input('Введите второе число: '))
if f < k:
    R = f+k**2 - 1
    print('if R = ',R)
elif f == 3 and k<2:
    R = k**2
    print('elif R = ',R)
else:
    R = f - 1
    print('else R = ',R)
