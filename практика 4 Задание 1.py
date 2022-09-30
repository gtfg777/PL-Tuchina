A = int(input("Введите первое число"))
B =  int(input("Введите второе число"))
if A < B:
    for x in range(A, B+1):
        print(x,sep = ' ')
else:
    for x in range(A, B-1):
        print(x,sep = ' ')
