import math
n, m = map(int, input('Введите аргументы через пробел:').split())
i = 1
while True:
    print(i, end='')
    i = 1 + (i + m - 2) % n
    if i == 1:
        break
print()