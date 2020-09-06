def fib(n):
    v = -1
    v2 = 1
    i = 0
    while i < n:
        tmp = v2
        v2 += v
        v = tmp
        if not v2 % 2:
            i += 1
            yield v2


print(*fib(int(input('Введите число элементов последовательности: '))))